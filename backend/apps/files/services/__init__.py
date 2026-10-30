from .storage_base import BaseStorageService
from .s3_service import S3StorageService, S3StorageError, S3PreconditionFailedError
from .key_generator import ObjectKeyGenerator

def get_storage_service() -> BaseStorageService:
    """Return configured storage provider service instance."""
    return S3StorageService()

__all__ = [
    'BaseStorageService',
    'S3StorageService',
    'S3StorageError',
    'S3PreconditionFailedError',
    'ObjectKeyGenerator',
    'get_storage_service',
]
