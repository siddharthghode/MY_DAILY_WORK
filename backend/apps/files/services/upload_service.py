import logging
import uuid
from datetime import timedelta
from typing import Dict, Any, Optional
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from .storage_base import BaseStorageService
from .key_generator import ObjectKeyGenerator
from .integrity_service import IntegrityService, IntegrityVerificationError

logger = logging.getLogger(__name__)

class UploadServiceError(Exception):
    """Base exception for upload service errors."""
    pass

class UploadService:
    """
    Orchestrates Backend-Mediated (Mode A) and Direct Pre-Signed (Mode B) upload workflows.
    Ensures state machine transitions and database/storage consistency.
    """

    def __init__(self, storage_service: BaseStorageService):
        self.storage = storage_service

    def backend_mediated_upload(
        self,
        user,
        fileobj,
        original_filename: str,
        content_type: str,
        file_size: int,
        tenant_id: Optional[str] = None,
        is_public: bool = False,
        metadata: Optional[Dict[str, Any]] = None,
        if_none_match: bool = False
    ) -> StoredFile:
        """
        Mode A: Backend-mediated streaming upload.
        Restricted to small files (< BACKEND_MEDIATED_MAX_BYTES).
        Streams data to S3 without buffering entire payload into application memory.
        Uses compensating actions to delete uploaded bytes if database persistence fails.
        """
        max_bytes = getattr(settings, 'BACKEND_MEDIATED_MAX_BYTES', 10 * 1024 * 1024)
        if file_size > max_bytes:
            raise UploadServiceError(
                f"File size {file_size} exceeds backend-mediated limit of {max_bytes} bytes. Use direct upload."
            )

        effective_tenant = tenant_id or getattr(getattr(user, 'profile', None), 'tenant_id', f"tenant_{user.id}")
        file_id = uuid.uuid4()
        object_key = ObjectKeyGenerator.generate_tenant_key(
            tenant_id=effective_tenant,
            file_id=file_id,
            original_filename=original_filename,
            is_public=is_public
        )

        uploaded_to_s3 = False
        try:
            # Stream payload directly to S3
            put_result = self.storage.put_object_stream(
                object_key=object_key,
                fileobj=fileobj,
                content_type=content_type,
                content_length=file_size,
                if_none_match=if_none_match
            )
            uploaded_to_s3 = True

            now = timezone.now()
            with transaction.atomic():
                stored_file = StoredFile.objects.create(
                    id=file_id,
                    owner=user,
                    tenant_id=effective_tenant,
                    object_key=object_key,
                    storage_provider='s3',
                    bucket_name=getattr(self.storage, 'bucket_name', 'default'),
                    original_filename=original_filename,
                    content_type=content_type,
                    expected_size=file_size,
                    verified_size=file_size,
                    etag=put_result.get('etag'),
                    version_id=put_result.get('version_id'),
                    status=FileStatus.COMPLETED,
                    is_public=is_public,
                    metadata=metadata or {},
                    completed_at=now
                )

                UploadSession.objects.create(
                    owner=user,
                    tenant_id=effective_tenant,
                    file=stored_file,
                    upload_mode=UploadMode.BACKEND_MEDIATED,
                    expected_size=file_size,
                    expected_content_type=content_type,
                    part_size=file_size,
                    total_parts=1,
                    status=FileStatus.COMPLETED,
                    expires_at=now,
                    completed_at=now
                )

            logger.info("Backend-mediated upload %s completed successfully.", file_id)
            return stored_file

        except Exception as e:
            # Compensating action: remove orphaned S3 object if database write failed
            if uploaded_to_s3:
                logger.warning("Compensating action: Deleting orphaned object %s after error: %s", object_key, e)
                try:
                    self.storage.delete_object(object_key)
                except Exception as del_err:
                    logger.error("Failed compensating deletion of %s: %s", object_key, del_err)

            raise UploadServiceError(f"Backend upload failed: {e}")

    def init_direct_upload(
        self,
        user,
        original_filename: str,
        content_type: str,
        expected_size: int,
        tenant_id: Optional[str] = None,
        is_public: bool = False,
        use_post_policy: bool = True,
        metadata: Optional[Dict[str, Any]] = None,
        expires_in_seconds: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Mode B: Initiates a direct client-to-S3 upload session.
        Generates restricted upload capability (pre-signed POST policy or pre-signed PUT URL).
        """
        max_file_size = getattr(settings, 'UPLOAD_MAX_FILE_SIZE_BYTES', 5 * 1024 * 1024 * 1024)
        if expected_size > max_file_size:
            raise UploadServiceError(f"File size {expected_size} exceeds maximum limit of {max_file_size} bytes.")

        effective_tenant = tenant_id or getattr(getattr(user, 'profile', None), 'tenant_id', f"tenant_{user.id}")
        file_id = uuid.uuid4()
        object_key = ObjectKeyGenerator.generate_tenant_key(
            tenant_id=effective_tenant,
            file_id=file_id,
            original_filename=original_filename,
            is_public=is_public
        )

        expiry = expires_in_seconds or getattr(settings, 'PRESIGNED_URL_EXPIRY_SECONDS', 3600)
        expires_at = timezone.now() + timedelta(seconds=expiry)

        with transaction.atomic():
            stored_file = StoredFile.objects.create(
                id=file_id,
                owner=user,
                tenant_id=effective_tenant,
                object_key=object_key,
                storage_provider='s3',
                bucket_name=getattr(self.storage, 'bucket_name', 'default'),
                original_filename=original_filename,
                content_type=content_type,
                expected_size=expected_size,
                status=FileStatus.UPLOADING,
                is_public=is_public,
                metadata=metadata or {},
                expired_at=expires_at
            )

            session = UploadSession.objects.create(
                owner=user,
                tenant_id=effective_tenant,
                file=stored_file,
                upload_mode=UploadMode.DIRECT_SINGLE,
                expected_size=expected_size,
                expected_content_type=content_type,
                part_size=expected_size,
                total_parts=1,
                status=FileStatus.UPLOADING,
                expires_at=expires_at
            )

        response_data: Dict[str, Any] = {
            'upload_id': str(session.id),
            'file_id': str(stored_file.id),
            'object_key': object_key,
            'expires_at': expires_at.isoformat(),
        }

        if use_post_policy:
            # POST policy enforces content-length-range server-side in S3
            post_data = self.storage.generate_presigned_post_policy(
                object_key=object_key,
                content_type=content_type,
                min_size=1,
                max_size=expected_size,
                expires_in=expiry
            )
            response_data['upload_method'] = 'POST'
            response_data['post_url'] = post_data['url']
            response_data['post_fields'] = post_data['fields']
        else:
            put_url = self.storage.generate_presigned_put_url(
                object_key=object_key,
                content_type=content_type,
                expires_in=expiry
            )
            response_data['upload_method'] = 'PUT'
            response_data['put_url'] = put_url

        return response_data

    def complete_direct_upload(
        self,
        session_id: str,
        user,
        expected_checksum: Optional[str] = None
    ) -> StoredFile:
        """
        Completes direct upload session after client has finished S3 transfer.
        Runs HEAD request against S3 to verify size, content type, and ETag.
        Idempotent with row locking to prevent race conditions.
        """
        try:
            with transaction.atomic():
                session = (
                    UploadSession.objects.select_for_update()
                    .select_related('file')
                    .filter(id=session_id)
                    .first()
                )

                if not session:
                    raise UploadServiceError("Upload session not found.")

                # Idempotency check: if already completed, return existing file
                if session.status == FileStatus.COMPLETED and session.file.status == FileStatus.COMPLETED:
                    logger.info("Direct upload session %s already completed (idempotent call).", session.id)
                    return session.file

                if session.owner != user and not user.is_staff:
                    raise UploadServiceError("Unauthorized: You do not own this upload session.")

                if session.is_expired:
                    session.status = FileStatus.EXPIRED
                    session.save(update_fields=['status'])
                    raise UploadServiceError("Upload session has expired.")

                if session.status in (FileStatus.ABORTED, FileStatus.FAILED):
                    raise UploadServiceError(f"Cannot complete session in state {session.status}.")

                head_data = self.storage.head_object(session.file.object_key)
                if not head_data:
                    raise IntegrityVerificationError("Verification failed: object was not uploaded to storage.")

                IntegrityService.verify_object_metadata(
                    head_data=head_data,
                    expected_size=session.expected_size,
                    expected_content_type=session.expected_content_type,
                    expected_checksum=expected_checksum
                )

                now = timezone.now()
                file_obj = session.file
                file_obj.verified_size = head_data['content_length']
                file_obj.etag = head_data.get('etag')
                file_obj.version_id = head_data.get('version_id')
                if expected_checksum:
                    file_obj.checksum = expected_checksum
                    file_obj.checksum_algorithm = 'MD5'
                file_obj.status = FileStatus.COMPLETED
                file_obj.completed_at = now
                file_obj.save()

                session.status = FileStatus.COMPLETED
                session.completed_at = now
                session.save(update_fields=['status', 'completed_at'])

                logger.info("Direct upload session %s completed and verified successfully.", session.id)
                return file_obj

        except IntegrityVerificationError as err:
            # Persist failure state outside of rolled back atomic transaction
            UploadSession.objects.filter(id=session_id).update(
                status=FileStatus.FAILED,
                error_message=str(err)
            )
            StoredFile.objects.filter(upload_sessions__id=session_id).update(
                status=FileStatus.FAILED
            )
            raise UploadServiceError(str(err))

