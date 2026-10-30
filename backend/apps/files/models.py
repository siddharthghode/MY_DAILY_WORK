import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class FileStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    UPLOADING = 'UPLOADING', 'Uploading'
    VERIFYING = 'VERIFYING', 'Verifying'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'
    ABORTED = 'ABORTED', 'Aborted'
    EXPIRED = 'EXPIRED', 'Expired'

class UploadMode(models.TextChoices):
    BACKEND_MEDIATED = 'BACKEND_MEDIATED', 'Backend Mediated'
    DIRECT_SINGLE = 'DIRECT_SINGLE', 'Direct Single Pre-Signed'
    DIRECT_MULTIPART = 'DIRECT_MULTIPART', 'Direct Multipart'

class StoredFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    tenant_id = models.CharField(max_length=64, db_index=True)
    
    # Storage details
    object_key = models.CharField(max_length=1024, unique=True, db_index=True)
    storage_provider = models.CharField(max_length=64, default='s3')
    bucket_name = models.CharField(max_length=255)
    
    # Metadata
    original_filename = models.CharField(max_length=255)
    content_type = models.CharField(max_length=128)
    expected_size = models.BigIntegerField()
    verified_size = models.BigIntegerField(null=True, blank=True)
    
    # Checksum and ETag
    etag = models.CharField(max_length=128, null=True, blank=True)
    checksum = models.CharField(max_length=128, null=True, blank=True)
    checksum_algorithm = models.CharField(max_length=32, blank=True, default='')
    version_id = models.CharField(max_length=128, null=True, blank=True)
    
    # Status and flags
    status = models.CharField(
        max_length=32,
        choices=FileStatus.choices,
        default=FileStatus.PENDING,
        db_index=True
    )
    is_public = models.BooleanField(default=False)
    metadata = models.JSONField(default=dict, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['tenant_id', 'status']),
            models.Index(fields=['owner', 'created_at']),
            models.Index(fields=['status', 'created_at']),
        ]

    def __str__(self):
        return f"{self.original_filename} ({self.id}) - {self.status}"

    @property
    def is_completed(self):
        return self.status == FileStatus.COMPLETED

class UploadSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upload_sessions')
    tenant_id = models.CharField(max_length=64, db_index=True)
    file = models.ForeignKey(StoredFile, on_delete=models.CASCADE, related_name='upload_sessions')
    
    upload_mode = models.CharField(
        max_length=32,
        choices=UploadMode.choices,
        default=UploadMode.DIRECT_SINGLE
    )
    provider_upload_id = models.CharField(max_length=255, null=True, blank=True)
    
    # Sizing
    expected_size = models.BigIntegerField()
    expected_content_type = models.CharField(max_length=128)
    part_size = models.BigIntegerField(null=True, blank=True)
    total_parts = models.PositiveIntegerField(default=1)
    
    # Lifecycle state
    status = models.CharField(
        max_length=32,
        choices=FileStatus.choices,
        default=FileStatus.PENDING,
        db_index=True
    )
    error_message = models.TextField(blank=True, default='')
    
    # Timestamps
    expires_at = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['owner', 'status']),
            models.Index(fields=['expires_at', 'status']),
            models.Index(fields=['provider_upload_id']),
        ]

    def __str__(self):
        return f"Session {self.id} for {self.file_id} [{self.status}]"

    @property
    def is_expired(self):
        return timezone.now() >= self.expires_at

class UploadedPart(models.Model):
    id = models.BigAutoField(primary_key=True)
    upload_session = models.ForeignKey(
        UploadSession,
        on_delete=models.CASCADE,
        related_name='parts'
    )
    part_number = models.PositiveIntegerField()
    etag = models.CharField(max_length=128)
    size = models.BigIntegerField(null=True, blank=True)
    checksum = models.CharField(max_length=128, blank=True, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['part_number']
        unique_together = ('upload_session', 'part_number')
        indexes = [
            models.Index(fields=['upload_session', 'part_number']),
        ]

    def __str__(self):
        return f"Part {self.part_number} for Session {self.upload_session_id} (ETag: {self.etag})"
