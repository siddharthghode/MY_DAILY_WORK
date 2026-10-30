import logging
from typing import Dict, Any, Optional, List
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from django.conf import settings
from .storage_base import BaseStorageService

logger = logging.getLogger(__name__)

class S3PreconditionFailedError(Exception):
    """Raised when an S3 conditional write fails (HTTP 412 Precondition Failed)."""
    pass

class S3StorageError(Exception):
    """General S3 storage operation error."""
    pass

class S3StorageService(BaseStorageService):
    """
    Production-grade S3 and S3-compatible (MinIO, R2, Ceph) storage provider implementation.
    """

    def __init__(
        self,
        bucket_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        region_name: Optional[str] = None,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
    ):
        self.bucket_name = bucket_name or getattr(settings, 'AWS_STORAGE_BUCKET_NAME', 'default-bucket')
        self.endpoint_url = endpoint_url or getattr(settings, 'AWS_S3_ENDPOINT_URL', None)
        self.region_name = region_name or getattr(settings, 'AWS_S3_REGION_NAME', 'us-east-1')
        self.access_key = access_key or getattr(settings, 'AWS_ACCESS_KEY_ID', None)
        self.secret_key = secret_key or getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)

        config_kwargs: Dict[str, Any] = {
            'signature_version': getattr(settings, 'AWS_S3_SIGNATURE_VERSION', 's3v4'),
        }
        # If using a custom endpoint (such as MinIO), enable path-style addressing
        if self.endpoint_url:
            config_kwargs['s3'] = {'addressing_style': 'path'}

        self.client = boto3.client(
            's3',
            endpoint_url=self.endpoint_url,
            region_name=self.region_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            config=Config(**config_kwargs)
        )

    def generate_presigned_put_url(
        self,
        object_key: str,
        content_type: str,
        expires_in: int = 3600,
        metadata: Optional[Dict[str, str]] = None
    ) -> str:
        params: Dict[str, Any] = {
            'Bucket': self.bucket_name,
            'Key': object_key,
            'ContentType': content_type,
        }
        if metadata:
            params['Metadata'] = metadata

        try:
            url = self.client.generate_presigned_url(
                ClientMethod='put_object',
                Params=params,
                ExpiresIn=expires_in
            )
            return url
        except ClientError as e:
            logger.error("Failed to generate presigned PUT URL for key %s: %s", object_key, e)
            raise S3StorageError(f"Failed to generate upload URL: {e}")

    def generate_presigned_post_policy(
        self,
        object_key: str,
        content_type: str,
        min_size: int,
        max_size: int,
        expires_in: int = 3600
    ) -> Dict[str, Any]:
        """
        Generates a pre-signed POST policy.
        Enforces both content-type and content-length-range server-side in S3.
        """
        fields = {
            'Content-Type': content_type,
        }
        conditions = [
            ['content-length-range', min_size, max_size],
            {'Content-Type': content_type},
        ]

        try:
            post_policy = self.client.generate_presigned_post(
                Bucket=self.bucket_name,
                Key=object_key,
                Fields=fields,
                Conditions=conditions,
                ExpiresIn=expires_in
            )
            return post_policy
        except ClientError as e:
            logger.error("Failed to generate presigned POST policy for key %s: %s", object_key, e)
            raise S3StorageError(f"Failed to generate upload policy: {e}")

    def initiate_multipart_upload(
        self,
        object_key: str,
        content_type: str,
        metadata: Optional[Dict[str, str]] = None
    ) -> str:
        params: Dict[str, Any] = {
            'Bucket': self.bucket_name,
            'Key': object_key,
            'ContentType': content_type,
        }
        if metadata:
            params['Metadata'] = metadata

        try:
            response = self.client.create_multipart_upload(**params)
            upload_id = response['UploadId']
            logger.info("Initiated multipart upload for key %s with ID %s", object_key, upload_id)
            return upload_id
        except ClientError as e:
            logger.error("Failed to initiate multipart upload for %s: %s", object_key, e)
            raise S3StorageError(f"Failed to initiate multipart upload: {e}")

    def generate_presigned_part_url(
        self,
        object_key: str,
        upload_id: str,
        part_number: int,
        expires_in: int = 3600
    ) -> str:
        try:
            url = self.client.generate_presigned_url(
                ClientMethod='upload_part',
                Params={
                    'Bucket': self.bucket_name,
                    'Key': object_key,
                    'UploadId': upload_id,
                    'PartNumber': part_number,
                },
                ExpiresIn=expires_in
            )
            return url
        except ClientError as e:
            logger.error("Failed to generate part URL for %s part %d: %s", object_key, part_number, e)
            raise S3StorageError(f"Failed to generate part upload URL: {e}")

    def complete_multipart_upload(
        self,
        object_key: str,
        upload_id: str,
        parts: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Completes a multipart upload. Parts must be a list of {'PartNumber': int, 'ETag': str}.
        """
        # Ensure parts are sorted by PartNumber as required by S3 specification
        sorted_parts = sorted(parts, key=lambda x: x['PartNumber'])
        # Strip extraneous quotes if already wrapped
        formatted_parts = [
            {
                'PartNumber': p['PartNumber'],
                'ETag': p['ETag'] if p['ETag'].startswith('"') else f'"{p["ETag"]}"'
            }
            for p in sorted_parts
        ]

        try:
            response = self.client.complete_multipart_upload(
                Bucket=self.bucket_name,
                Key=object_key,
                UploadId=upload_id,
                MultipartUpload={'Parts': formatted_parts}
            )
            logger.info("Completed multipart upload for key %s", object_key)
            return response
        except ClientError as e:
            logger.error("Failed to complete multipart upload for %s: %s", object_key, e)
            raise S3StorageError(f"Failed to complete multipart upload: {e}")

    def abort_multipart_upload(self, object_key: str, upload_id: str) -> None:
        try:
            self.client.abort_multipart_upload(
                Bucket=self.bucket_name,
                Key=object_key,
                UploadId=upload_id
            )
            logger.info("Aborted multipart upload %s for key %s", upload_id, object_key)
        except ClientError as e:
            logger.warning("Failed to abort multipart upload %s: %s", upload_id, e)

    def list_parts(self, object_key: str, upload_id: str) -> List[Dict[str, Any]]:
        parts: List[Dict[str, Any]] = []
        part_number_marker = 0

        while True:
            try:
                response = self.client.list_parts(
                    Bucket=self.bucket_name,
                    Key=object_key,
                    UploadId=upload_id,
                    PartNumberMarker=part_number_marker
                )
                for part in response.get('Parts', []):
                    parts.append({
                        'PartNumber': part['PartNumber'],
                        'ETag': part['ETag'].strip('"'),
                        'Size': part['Size'],
                        'LastModified': part['LastModified']
                    })

                if response.get('IsTruncated', False):
                    part_number_marker = response.get('NextPartNumberMarker', 0)
                else:
                    break
            except ClientError as e:
                logger.error("Failed listing parts for upload %s: %s", upload_id, e)
                raise S3StorageError(f"Failed listing parts: {e}")

        return parts

    def head_object(self, object_key: str) -> Optional[Dict[str, Any]]:
        try:
            response = self.client.head_object(
                Bucket=self.bucket_name,
                Key=object_key
            )
            return {
                'content_length': response.get('ContentLength', 0),
                'content_type': response.get('ContentType', ''),
                'etag': response.get('ETag', '').strip('"'),
                'version_id': response.get('VersionId'),
                'last_modified': response.get('LastModified'),
                'metadata': response.get('Metadata', {})
            }
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code')
            if error_code in ('404', 'NoSuchKey', 'NotFound'):
                return None
            logger.error("Error executing HEAD request on key %s: %s", object_key, e)
            raise S3StorageError(f"Failed inspecting object metadata: {e}")

    def put_object_stream(
        self,
        object_key: str,
        fileobj: Any,
        content_type: str,
        content_length: Optional[int] = None,
        if_none_match: bool = False
    ) -> Dict[str, Any]:
        """
        Streams a file object directly to S3.
        Supports conditional writes via `If-None-Match: *` to prevent overwriting existing keys.
        """
        put_kwargs: Dict[str, Any] = {
            'Bucket': self.bucket_name,
            'Key': object_key,
            'Body': fileobj,
            'ContentType': content_type,
        }
        if content_length is not None:
            put_kwargs['ContentLength'] = content_length
        if if_none_match:
            put_kwargs['IfNoneMatch'] = '*'

        try:
            response = self.client.put_object(**put_kwargs)
            return {
                'etag': response.get('ETag', '').strip('"'),
                'version_id': response.get('VersionId'),
            }
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code')
            if error_code in ('PreconditionFailed', '412'):
                logger.warning("Conditional write failed for key %s (already exists)", object_key)
                raise S3PreconditionFailedError(f"Object {object_key} already exists.")
            logger.error("Failed streaming upload for key %s: %s", object_key, e)
            raise S3StorageError(f"Streaming upload failed: {e}")

    def generate_presigned_get_url(
        self,
        object_key: str,
        expires_in: int = 900,
        filename_override: Optional[str] = None,
        response_content_type: Optional[str] = None
    ) -> str:
        params: Dict[str, Any] = {
            'Bucket': self.bucket_name,
            'Key': object_key,
        }
        if filename_override:
            safe_name = filename_override.replace('"', '\\"')
            params['ResponseContentDisposition'] = f'attachment; filename="{safe_name}"'
        if response_content_type:
            params['ResponseContentType'] = response_content_type

        try:
            return self.client.generate_presigned_url(
                ClientMethod='get_object',
                Params=params,
                ExpiresIn=expires_in
            )
        except ClientError as e:
            logger.error("Failed generating presigned GET for %s: %s", object_key, e)
            raise S3StorageError(f"Failed to generate download URL: {e}")

    def delete_object(self, object_key: str) -> bool:
        try:
            self.client.delete_object(Bucket=self.bucket_name, Key=object_key)
            logger.info("Deleted object %s from bucket %s", object_key, self.bucket_name)
            return True
        except ClientError as e:
            logger.error("Failed to delete object %s: %s", object_key, e)
            return False
