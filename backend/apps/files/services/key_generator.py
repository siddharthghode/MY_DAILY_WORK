import os
import re
import unicodedata
import uuid
from datetime import datetime

class ObjectKeyGenerator:
    """
    Generates safe, structured, high-entropy object keys for S3-compatible storage.
    Enforces tenant scoping, prevents path traversal, and supports content-addressed keys.
    """

    @staticmethod
    def sanitize_filename(filename: str, max_length: int = 255) -> str:
        """
        Sanitize user-supplied filename to prevent directory traversal and header injection.
        Strips path components, null bytes, and non-printable characters.
        """
        if not filename:
            return "unnamed_file"

        # Remove null bytes and control characters
        filename = "".join(ch for ch in filename if ch.isprintable() and ch != '\x00')

        # Normalize unicode (NFKD)
        filename = unicodedata.normalize('NFKD', filename)

        # Strip any leading directories / traversal attacks (e.g., ../../../etc/passwd)
        filename = os.path.basename(filename.replace('\\', '/'))

        # Strip dangerous characters, keeping alphanumeric, dots, underscores, and dashes
        filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)

        # Avoid empty or dot-only filenames (e.g. '.', '..', '.hidden')
        filename = filename.lstrip('.')
        if not filename:
            filename = "file"

        if len(filename) > max_length:
            name, ext = os.path.splitext(filename)
            ext = ext[:16]
            filename = name[: max_length - len(ext)] + ext

        return filename

    @classmethod
    def generate_tenant_key(
        cls,
        tenant_id: str,
        file_id: uuid.UUID,
        original_filename: str,
        is_public: bool = False
    ) -> str:
        """
        Generates a server-controlled, tenant-isolated object key.
        Format:
          tenants/<tenant_id>/files/<YYYY>/<MM>/<file_uuid>/<sanitized_filename>
          or public/files/<file_uuid>/<sanitized_filename>
        """
        sanitized_tenant = re.sub(r'[^a-zA-Z0-9_-]', '_', str(tenant_id or 'default'))
        safe_filename = cls.sanitize_filename(original_filename)
        now = datetime.utcnow()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        file_uuid_str = str(file_id)

        if is_public:
            return f"public/files/{year}/{month}/{file_uuid_str}/{safe_filename}"
        
        return f"tenants/{sanitized_tenant}/files/{year}/{month}/{file_uuid_str}/{safe_filename}"

    @classmethod
    def generate_content_addressed_key(cls, sha256_hex: str, original_filename: str) -> str:
        """
        Generates a content-addressed key based on the object's cryptographic digest.
        Ideal for deduplicated, public, or immutable assets.
        Format: cas/<prefix_2>/<sha256_hash>/<sanitized_filename>
        """
        safe_hash = re.sub(r'[^a-fA-F0-9]', '', sha256_hex.lower())
        if len(safe_hash) < 64:
            raise ValueError("Invalid SHA-256 hash length for content-addressed key.")
        prefix = safe_hash[:2]
        safe_filename = cls.sanitize_filename(original_filename)
        return f"cas/{prefix}/{safe_hash}/{safe_filename}"
