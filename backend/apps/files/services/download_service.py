import logging
from typing import Dict, Any, Optional
from django.conf import settings
from apps.files.models import StoredFile, FileStatus
from .storage_base import BaseStorageService

logger = logging.getLogger(__name__)

class DownloadServiceError(Exception):
    """Base exception for download service errors."""
    pass

class DownloadService:
    """
    Handles secure pre-signed download URL generation and CDN asset routing.
    Enforces authorization, tenant isolation, and file availability.
    """

    def __init__(self, storage_service: BaseStorageService):
        self.storage = storage_service

    def get_download_url(
        self,
        file_obj: StoredFile,
        user,
        expires_in_seconds: Optional[int] = None,
        as_attachment: bool = True
    ) -> Dict[str, Any]:
        """
        Generates a short-lived download URL for an authorized user.
        Bypasses Django for data transfer (zero proxy overhead, native HTTP Range support).
        """
        # Authorization check
        if not file_obj.is_public:
            if not user or not user.is_authenticated:
                raise DownloadServiceError("Authentication required for private file access.")
            
            # Tenant or owner validation
            user_tenant = getattr(getattr(user, 'profile', None), 'tenant_id', None)
            if file_obj.owner != user and (not user_tenant or user_tenant != file_obj.tenant_id) and not user.is_staff:
                raise DownloadServiceError("Access denied: You do not have permission to download this file.")

        # Availability check
        if file_obj.status != FileStatus.COMPLETED:
            raise DownloadServiceError(f"File is not available for download (status: {file_obj.status}).")

        cdn_base_url = getattr(settings, 'CDN_BASE_URL', '').rstrip('/')
        expiry = expires_in_seconds or getattr(settings, 'DOWNLOAD_URL_EXPIRY_SECONDS', 900)

        # If file is public and CDN is configured, route to CDN
        if file_obj.is_public and cdn_base_url:
            cdn_url = f"{cdn_base_url}/{file_obj.object_key}"
            logger.info("Generated CDN URL for public file %s", file_obj.id)
            return {
                'url': cdn_url,
                'delivery_method': 'CDN',
                'expires_at': None,
                'supports_ranges': True,
                'content_type': file_obj.content_type,
            }

        # Otherwise generate pre-signed S3 GET URL
        filename_override = file_obj.original_filename if as_attachment else None
        presigned_url = self.storage.generate_presigned_get_url(
            object_key=file_obj.object_key,
            expires_in=expiry,
            filename_override=filename_override,
            response_content_type=file_obj.content_type
        )

        logger.info("Generated presigned GET URL for file %s (user: %s)", file_obj.id, user.username if user else 'anonymous')
        return {
            'url': presigned_url,
            'delivery_method': 'PRESIGNED_S3',
            'expires_in_seconds': expiry,
            'supports_ranges': True,
            'content_type': file_obj.content_type,
            'filename': file_obj.original_filename,
            'size': file_obj.verified_size or file_obj.expected_size
        }
