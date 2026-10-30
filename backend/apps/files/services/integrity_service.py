import re
import hashlib
from typing import Optional, Dict, Any

class IntegrityVerificationError(Exception):
    """Raised when file integrity verification fails."""
    pass

class IntegrityService:
    """
    Handles file verification, ETags, and checksum integrity.
    Accounts for difference between single-part PUT ETags and multipart ETags.
    """

    @staticmethod
    def is_multipart_etag(etag: str) -> bool:
        """
        Multipart ETags in S3 follow the pattern: "<32-hex-chars>-<part_count>"
        e.g., "d41d8cd98f00b204e9800998ecf8427e-12"
        """
        clean_etag = etag.strip('"')
        return bool(re.match(r'^[a-fA-F0-9]{32}-\d+$', clean_etag))

    @staticmethod
    def verify_single_part_md5(expected_md5_hex: str, actual_etag: str) -> bool:
        """
        Verifies single-part upload ETag against expected MD5.
        NOTE: Only valid for single PUT uploads without KMS customer-managed keys.
        """
        clean_expected = expected_md5_hex.strip('"').lower()
        clean_actual = actual_etag.strip('"').lower()
        return clean_expected == clean_actual

    @classmethod
    def verify_object_metadata(
        cls,
        head_data: Dict[str, Any],
        expected_size: int,
        expected_content_type: Optional[str] = None,
        expected_checksum: Optional[str] = None
    ) -> bool:
        """
        Verifies that an uploaded object in S3 matches expected size, content-type,
        and optional checksum without downloading the entire object payload.
        """
        actual_size = head_data.get('content_length', 0)
        if actual_size != expected_size:
            raise IntegrityVerificationError(
                f"File size mismatch: expected {expected_size} bytes, found {actual_size} bytes."
            )

        if expected_content_type:
            actual_content_type = head_data.get('content_type', '')
            # Allow base type match (ignoring charset parameters)
            if expected_content_type.split(';')[0].lower() not in actual_content_type.lower():
                raise IntegrityVerificationError(
                    f"Content-Type mismatch: expected {expected_content_type}, found {actual_content_type}."
                )

        if expected_checksum:
            actual_etag = head_data.get('etag', '')
            if not cls.is_multipart_etag(actual_etag):
                if not cls.verify_single_part_md5(expected_checksum, actual_etag):
                    raise IntegrityVerificationError(
                        f"Checksum mismatch: expected {expected_checksum}, found ETag {actual_etag}."
                    )

        return True

    @staticmethod
    def compute_stream_sha256(fileobj, chunk_size: int = 65536) -> str:
        """
        Computes SHA-256 digest of a readable stream without loading all bytes in RAM.
        """
        sha = hashlib.sha256()
        current_pos = fileobj.tell() if hasattr(fileobj, 'tell') else 0
        try:
            while True:
                chunk = fileobj.read(chunk_size)
                if not chunk:
                    break
                sha.update(chunk)
            return sha.hexdigest()
        finally:
            if hasattr(fileobj, 'seek'):
                fileobj.seek(current_pos)
