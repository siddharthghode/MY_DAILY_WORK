import logging
import os
import subprocess
import shutil
import tempfile
from celery import shared_task
from django.utils import timezone
from apps.files.models import StoredFile, FileStatus
from apps.files.services import get_storage_service
from apps.files.services.cleanup_service import CleanupService

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_video_transcoding(self, file_id: str):
    """
    Optional asynchronous media processing pipeline:
    - Verifies completed original upload
    - Generates lightweight web preview / rendition using safe subprocess isolation
    - Uploads rendition to S3
    - Updates file metadata with rendition keys
    """
    storage = get_storage_service()
    try:
        file_obj = StoredFile.objects.get(id=file_id, status=FileStatus.COMPLETED)
    except StoredFile.DoesNotExist:
        logger.warning("Video transcoding skipped: StoredFile %s not found or not completed.", file_id)
        return

    # Check if FFmpeg is installed on host system
    ffmpeg_bin = shutil.which('ffmpeg')
    if not ffmpeg_bin:
        logger.info("FFmpeg binary not detected on host system. Simulating metadata probe.")
        file_obj.metadata['transcoding'] = {
            'status': 'skipped_no_ffmpeg',
            'processed_at': timezone.now().isoformat()
        }
        file_obj.save(update_fields=['metadata'])
        return

    with tempfile.TemporaryDirectory() as tmp_dir:
        input_path = os.path.join(tmp_dir, 'source_media')
        output_path = os.path.join(tmp_dir, 'preview.mp4')

        try:
            # Download URL to stream input
            dl_info = storage.generate_presigned_get_url(file_obj.object_key, expires_in=1800)
            
            # Run FFmpeg with safe resource limits and timeout
            cmd = [
                ffmpeg_bin,
                '-y',
                '-i', dl_info,
                '-t', '10',  # 10 second preview
                '-vf', 'scale=640:-2',
                '-c:v', 'libx264',
                '-preset', 'veryfast',
                '-crf', '28',
                '-movflags', '+faststart',
                output_path
            ]
            
            # Controlled execution with timeout and bounded output
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=120,
                check=True
            )

            # Upload preview to S3
            preview_key = f"{os.path.splitext(file_obj.object_key)[0]}_preview.mp4"
            with open(output_path, 'rb') as f:
                storage.put_object_stream(
                    object_key=preview_key,
                    fileobj=f,
                    content_type='video/mp4',
                    content_length=os.path.getsize(output_path)
                )

            file_obj.metadata['renditions'] = {
                'preview_key': preview_key,
                'preview_type': 'video/mp4',
                'transcoded_at': timezone.now().isoformat()
            }
            file_obj.save(update_fields=['metadata'])
            logger.info("Successfully transcoded preview for file %s", file_id)

        except subprocess.TimeoutExpired:
            logger.error("FFmpeg transcoding timed out for file %s", file_id)
            file_obj.metadata['transcoding'] = {'status': 'timeout'}
            file_obj.save(update_fields=['metadata'])
        except Exception as e:
            logger.error("FFmpeg processing failed for %s: %s", file_id, e)
            file_obj.metadata['transcoding'] = {'status': 'failed', 'error': str(e)}
            file_obj.save(update_fields=['metadata'])
            raise self.retry(exc=e)

@shared_task
def cleanup_stale_sessions_task():
    """Periodic task: expires stale sessions and aborts incomplete multipart uploads."""
    storage = get_storage_service()
    service = CleanupService(storage)
    expired = service.expire_stale_sessions()
    aborted = service.abort_stale_multipart_uploads()
    logger.info("Periodic cleanup finished: expired %d sessions, aborted %d multipart uploads.", expired, aborted)
    return {'expired_sessions': expired, 'aborted_multipart': aborted}

@shared_task
def reconcile_storage_task():
    """Periodic task: reconciles pending files against S3 object store."""
    storage = get_storage_service()
    service = CleanupService(storage)
    result = service.reconcile_pending_files()
    logger.info("Periodic reconciliation finished: %s", result)
    return result
