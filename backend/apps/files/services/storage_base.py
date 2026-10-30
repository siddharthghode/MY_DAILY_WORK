from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List, Tuple

class BaseStorageService(ABC):
    """
    Abstract interface for S3-compatible cloud object storage providers.
    """

    @abstractmethod
    def generate_presigned_put_url(
        self,
        object_key: str,
        content_type: str,
        expires_in: int = 3600,
        metadata: Optional[Dict[str, str]] = None
    ) -> str:
        """Generate a pre-signed URL for direct HTTP PUT upload."""
        pass

    @abstractmethod
    def generate_presigned_post_policy(
        self,
        object_key: str,
        content_type: str,
        min_size: int,
        max_size: int,
        expires_in: int = 3600
    ) -> Dict[str, Any]:
        """Generate a pre-signed POST policy with enforced content-length range."""
        pass

    @abstractmethod
    def initiate_multipart_upload(
        self,
        object_key: str,
        content_type: str,
        metadata: Optional[Dict[str, str]] = None
    ) -> str:
        """Initiate multipart upload and return provider upload ID."""
        pass

    @abstractmethod
    def generate_presigned_part_url(
        self,
        object_key: str,
        upload_id: str,
        part_number: int,
        expires_in: int = 3600
    ) -> str:
        """Generate a pre-signed URL for uploading a specific multipart chunk."""
        pass

    @abstractmethod
    def complete_multipart_upload(
        self,
        object_key: str,
        upload_id: str,
        parts: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Finalize multipart upload with ordered parts list [{PartNumber: int, ETag: str}]."""
        pass

    @abstractmethod
    def abort_multipart_upload(self, object_key: str, upload_id: str) -> None:
        """Abort an abandoned multipart upload session."""
        pass

    @abstractmethod
    def list_parts(self, object_key: str, upload_id: str) -> List[Dict[str, Any]]:
        """List currently uploaded parts for a multipart session."""
        pass

    @abstractmethod
    def head_object(self, object_key: str) -> Optional[Dict[str, Any]]:
        """Retrieve metadata of an existing object without downloading its payload."""
        pass

    @abstractmethod
    def put_object_stream(
        self,
        object_key: str,
        fileobj: Any,
        content_type: str,
        content_length: Optional[int] = None,
        if_none_match: bool = False
    ) -> Dict[str, Any]:
        """Stream data directly to storage for backend-mediated uploads."""
        pass

    @abstractmethod
    def generate_presigned_get_url(
        self,
        object_key: str,
        expires_in: int = 900,
        filename_override: Optional[str] = None,
        response_content_type: Optional[str] = None
    ) -> str:
        """Generate a pre-signed GET URL for secure downloading."""
        pass

    @abstractmethod
    def delete_object(self, object_key: str) -> bool:
        """Delete an object from storage."""
        pass
