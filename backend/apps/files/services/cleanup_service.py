import logging
from typing import Dict, Any, List
from django.utils import timezone
from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from .storage_base import BaseStorageService

logger = logging.getLogger(__name__)

class CleanupService:
    """
    Automates storage reconciliation and cost management:
    - Expires abandoned upload sessions
    - Aborts stale multipart uploads in S3 to prevent ongoing storage charges
    - Cleans up orphaned or aborted objects
    - NEVER deletes completed user files during reconciliation
    """

    def __init__(self, storage_service: BaseStorageService):
        self.storage = storage_service

    def expire_stale_sessions(self) -> int:
        """
        Marks active upload sessions past their expires_at date as EXPIRED.
        """
        now = timezone.now()
        stale_sessions = UploadSession.objects.filter(
            status__in=[FileStatus.PENDING, FileStatus.UPLOADING, FileStatus.VERIFYING],
            expires_at__lt=now
        )
        count = 0
        for session in stale_sessions:
            session.status = FileStatus.EXPIRED
            session.save(update_fields=['status'])
            # Also expire associated file if not completed
            if session.file.status != FileStatus.COMPLETED:
                session.file.status = FileStatus.EXPIRED
                session.file.save(update_fields=['status'])
            count += 1

        logger.info("Marked %d stale upload sessions as EXPIRED.", count)
        return count

    def abort_stale_multipart_uploads(self) -> int:
        """
        Aborts abandoned S3 multipart uploads.
        Uncompleted multipart parts incur ongoing S3 storage costs unless explicitly aborted.
        """
        now = timezone.now()
        abandoned_sessions = UploadSession.objects.filter(
            upload_mode=UploadMode.DIRECT_MULTIPART,
            status__in=[FileStatus.EXPIRED, FileStatus.ABORTED],
            provider_upload_id__isnull=False
        ).select_related('file')

        aborted_count = 0
        for session in abandoned_sessions:
            if session.file.status == FileStatus.COMPLETED:
                continue  # Never abort if file is completed

            try:
                self.storage.abort_multipart_upload(
                    object_key=session.file.object_key,
                    upload_id=session.provider_upload_id
                )
                session.provider_upload_id = None
                session.save(update_fields=['provider_upload_id'])
                aborted_count += 1
                logger.info("Cleaned up S3 multipart session %s for key %s", session.id, session.file.object_key)
            except Exception as e:
                logger.warning("Failed aborting S3 multipart upload for session %s: %s", session.id, e)

        return aborted_count

    def reconcile_pending_files(self) -> Dict[str, int]:
        """
        Reconciles database files in VERIFYING state against actual S3 objects.
        """
        verifying_files = StoredFile.objects.filter(status=FileStatus.VERIFYING)
        reconciled = 0
        failed = 0

        for f in verifying_files:
            head = self.storage.head_object(f.object_key)
            if head and head['content_length'] == f.expected_size:
                f.status = FileStatus.COMPLETED
                f.verified_size = head['content_length']
                f.etag = head['etag']
                f.completed_at = timezone.now()
                f.save()
                reconciled += 1
            else:
                f.status = FileStatus.FAILED
                f.save(update_fields=['status'])
                failed += 1

        return {'reconciled': reconciled, 'failed': failed}
