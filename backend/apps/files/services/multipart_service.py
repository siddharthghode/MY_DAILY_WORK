import math
import logging
from datetime import timedelta
from typing import Dict, Any, List, Optional, Tuple
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from apps.files.models import StoredFile, UploadSession, UploadedPart, FileStatus, UploadMode
from .storage_base import BaseStorageService
from .key_generator import ObjectKeyGenerator
from .integrity_service import IntegrityService

logger = logging.getLogger(__name__)

class MultipartServiceError(Exception):
    """Base exception for multipart service errors."""
    pass

class MultipartService:
    """
    Manages end-to-end S3 multipart upload lifecycle:
    - Calculation of chunk sizes compliant with S3 constraints
    - Initiation & batched pre-signed URL generation
    - Tracking uploaded parts
    - Resuming interrupted sessions
    - Atomic completion and verification
    - Safe abortion of abandoned sessions
    """

    def __init__(self, storage_service: BaseStorageService):
        self.storage = storage_service

    @staticmethod
    def calculate_part_geometry(file_size: int) -> Tuple[int, int]:
        """
        Calculates part size and total parts adhering to S3 constraints:
        - Minimum part size: 5 MB (except final part)
        - Maximum part count: 10,000
        - Maximum object size: 5 TB
        """
        min_part_size = getattr(settings, 'MIN_PART_SIZE_BYTES', 5 * 1024 * 1024)
        default_part_size = getattr(settings, 'DEFAULT_PART_SIZE_BYTES', 10 * 1024 * 1024)
        max_part_count = getattr(settings, 'MAX_PART_COUNT', 10000)

        if file_size <= 0:
            raise MultipartServiceError("File size must be greater than zero for multipart upload.")

        # Minimum part size required so total parts <= 10,000
        required_min_part_size = math.ceil(file_size / max_part_count)

        part_size = max(default_part_size, required_min_part_size, min_part_size)
        total_parts = math.ceil(file_size / part_size)

        if total_parts > max_part_count:
            raise MultipartServiceError(
                f"File size exceeds maximum supported capacity within {max_part_count} parts."
            )

        return part_size, total_parts

    def initiate_multipart_session(
        self,
        user,
        original_filename: str,
        content_type: str,
        expected_size: int,
        tenant_id: Optional[str] = None,
        is_public: bool = False,
        metadata: Optional[Dict[str, Any]] = None,
        expires_in_seconds: Optional[int] = None
    ) -> UploadSession:
        """
        Initiates a multipart upload with S3 and creates DB tracking records.
        """
        effective_tenant = tenant_id or getattr(getattr(user, 'profile', None), 'tenant_id', f"tenant_{user.id}")
        part_size, total_parts = self.calculate_part_geometry(expected_size)

        # Temporary UUID for key generation
        import uuid
        temp_file_id = uuid.uuid4()
        object_key = ObjectKeyGenerator.generate_tenant_key(
            tenant_id=effective_tenant,
            file_id=temp_file_id,
            original_filename=original_filename,
            is_public=is_public
        )

        # Initiate on storage provider
        provider_upload_id = self.storage.initiate_multipart_upload(
            object_key=object_key,
            content_type=content_type,
            metadata={'original_filename': original_filename, 'tenant_id': effective_tenant}
        )

        expiry_seconds = expires_in_seconds or getattr(settings, 'PRESIGNED_URL_EXPIRY_SECONDS', 3600)
        expires_at = timezone.now() + timedelta(seconds=expiry_seconds)

        with transaction.atomic():
            stored_file = StoredFile.objects.create(
                id=temp_file_id,
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
                upload_mode=UploadMode.DIRECT_MULTIPART,
                provider_upload_id=provider_upload_id,
                expected_size=expected_size,
                expected_content_type=content_type,
                part_size=part_size,
                total_parts=total_parts,
                status=FileStatus.UPLOADING,
                expires_at=expires_at
            )

        return session

    def generate_part_urls(
        self,
        session: UploadSession,
        start_part: int = 1,
        count: int = 10,
        expires_in_seconds: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Generates a bounded batch of pre-signed PUT URLs for parts.
        """
        if session.is_expired or session.status in (FileStatus.COMPLETED, FileStatus.ABORTED, FileStatus.FAILED):
            raise MultipartServiceError(f"Upload session is not active (status: {session.status}).")

        expiry = expires_in_seconds or getattr(settings, 'PRESIGNED_URL_EXPIRY_SECONDS', 3600)
        max_batch = 50
        count = min(count, max_batch)

        end_part = min(start_part + count - 1, session.total_parts)
        urls = []

        for part_number in range(start_part, end_part + 1):
            url = self.storage.generate_presigned_part_url(
                object_key=session.file.object_key,
                upload_id=session.provider_upload_id,
                part_number=part_number,
                expires_in=expiry
            )
            urls.append({
                'part_number': part_number,
                'upload_url': url
            })

        return urls

    def record_uploaded_parts(
        self,
        session: UploadSession,
        parts_data: List[Dict[str, Any]]
    ) -> List[UploadedPart]:
        """
        Persists part numbers and ETags reported by the client or synced from S3.
        """
        saved_parts = []
        with transaction.atomic():
            for p in parts_data:
                part_obj, _ = UploadedPart.objects.update_or_create(
                    upload_session=session,
                    part_number=p['part_number'],
                    defaults={
                        'etag': p['etag'].strip('"'),
                        'size': p.get('size'),
                        'checksum': p.get('checksum', ''),
                    }
                )
                saved_parts.append(part_obj)
        return saved_parts

    def sync_parts_from_storage(self, session: UploadSession) -> List[Dict[str, Any]]:
        """
        Lists parts already successfully stored in S3 for resuming after interruption.
        """
        provider_parts = self.storage.list_parts(
            object_key=session.file.object_key,
            upload_id=session.provider_upload_id
        )

        formatted_parts = [
            {
                'part_number': p['PartNumber'],
                'etag': p['ETag'],
                'size': p['Size'],
            }
            for p in provider_parts
        ]
        self.record_uploaded_parts(session, formatted_parts)
        return formatted_parts

    def complete_multipart_session(
        self,
        session_id: str,
        user,
        client_parts: Optional[List[Dict[str, Any]]] = None
    ) -> StoredFile:
        """
        Finalizes multipart upload idempotently with row locking and object verification.
        """
        try:
            with transaction.atomic():
                # Acquire exclusive lock on UploadSession and StoredFile
                session = (
                    UploadSession.objects.select_for_update()
                    .select_related('file')
                    .filter(id=session_id)
                    .first()
                )

                if not session:
                    raise MultipartServiceError("Upload session not found.")

                # Idempotency check: if already completed, return file record
                if session.status == FileStatus.COMPLETED and session.file.status == FileStatus.COMPLETED:
                    logger.info("Upload session %s already completed (idempotent call).", session.id)
                    return session.file

                if session.owner != user and not user.is_staff:
                    raise MultipartServiceError("Unauthorized: You do not own this upload session.")

                if session.is_expired:
                    session.status = FileStatus.EXPIRED
                    session.save(update_fields=['status'])
                    raise MultipartServiceError("Upload session has expired.")

                if session.status in (FileStatus.ABORTED, FileStatus.FAILED):
                    raise MultipartServiceError(f"Cannot complete session in state {session.status}.")

                # Determine part list
                parts_to_commit: List[Dict[str, Any]] = []
                if client_parts:
                    parts_to_commit = [
                        {'PartNumber': int(p['part_number']), 'ETag': p['etag']}
                        for p in client_parts
                    ]
                else:
                    # Retrieve from database
                    db_parts = session.parts.order_by('part_number')
                    parts_to_commit = [
                        {'PartNumber': p.part_number, 'ETag': p.etag}
                        for p in db_parts
                    ]

                if len(parts_to_commit) != session.total_parts:
                    # Query S3 directly to see if all parts actually exist
                    synced = self.sync_parts_from_storage(session)
                    parts_to_commit = [
                        {'PartNumber': p['part_number'], 'ETag': p['etag']}
                        for p in synced
                    ]

                if len(parts_to_commit) != session.total_parts:
                    missing = session.total_parts - len(parts_to_commit)
                    raise MultipartServiceError(
                        f"Cannot complete upload: {missing} parts are missing out of {session.total_parts}."
                    )

                session.status = FileStatus.VERIFYING
                session.save(update_fields=['status'])

                # Call S3 CompleteMultipartUpload
                s3_response = self.storage.complete_multipart_upload(
                    object_key=session.file.object_key,
                    upload_id=session.provider_upload_id,
                    parts=parts_to_commit
                )

                # Verify completed object via HEAD request
                head_data = self.storage.head_object(session.file.object_key)
                if not head_data:
                    raise MultipartServiceError("Verification failed: object not found in storage.")

                IntegrityService.verify_object_metadata(
                    head_data=head_data,
                    expected_size=session.expected_size,
                    expected_content_type=session.expected_content_type
                )

                now = timezone.now()
                file_obj = session.file
                file_obj.verified_size = head_data['content_length']
                file_obj.etag = head_data.get('etag')
                file_obj.version_id = head_data.get('version_id')
                file_obj.status = FileStatus.COMPLETED
                file_obj.completed_at = now
                file_obj.save()

                session.status = FileStatus.COMPLETED
                session.completed_at = now
                session.save(update_fields=['status', 'completed_at'])

                logger.info("Multipart upload %s successfully completed and verified.", session.id)
                return file_obj

        except Exception as e:
            if not isinstance(e, MultipartServiceError) or "missing" not in str(e):
                UploadSession.objects.filter(id=session_id).update(
                    status=FileStatus.FAILED,
                    error_message=str(e)
                )
                StoredFile.objects.filter(upload_sessions__id=session_id).update(
                    status=FileStatus.FAILED
                )
            if isinstance(e, MultipartServiceError):
                raise
            raise MultipartServiceError(f"Storage completion failed: {e}")


    def abort_multipart_session(self, session_id: str, user) -> None:
        """
        Aborts an active multipart upload and frees associated cloud resources.
        """
        with transaction.atomic():
            session = (
                UploadSession.objects.select_for_update()
                .select_related('file')
                .filter(id=session_id)
                .first()
            )
            if not session:
                raise MultipartServiceError("Upload session not found.")

            if session.owner != user and not user.is_staff:
                raise MultipartServiceError("Unauthorized: You do not own this upload session.")

            if session.status == FileStatus.COMPLETED:
                raise MultipartServiceError("Cannot abort a completed upload session.")

            # Abort in storage provider
            if session.provider_upload_id:
                self.storage.abort_multipart_upload(
                    object_key=session.file.object_key,
                    upload_id=session.provider_upload_id
                )

            session.status = FileStatus.ABORTED
            session.save(update_fields=['status'])

            file_obj = session.file
            file_obj.status = FileStatus.ABORTED
            file_obj.save(update_fields=['status'])
            logger.info("Upload session %s aborted.", session.id)
