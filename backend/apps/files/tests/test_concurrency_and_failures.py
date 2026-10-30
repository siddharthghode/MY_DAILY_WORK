import io
import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from unittest.mock import patch

from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from apps.files.services.s3_service import S3StorageService
from apps.files.services.upload_service import UploadService, UploadServiceError
from apps.files.services.multipart_service import MultipartService, MultipartServiceError

@pytest.fixture
def fail_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')
        user = User.objects.create_user(username='concurrency_user', password='password123')
        yield {'storage': storage, 'user': user}

def test_compensating_action_on_db_failure(fail_setup):
    """
    If S3 write succeeds but database transaction raises an unexpected error,
    the uploaded object must be deleted to prevent orphaned bytes.
    """
    storage = fail_setup['storage']
    user = fail_setup['user']
    service = UploadService(storage)

    with patch('apps.files.models.StoredFile.objects.create', side_effect=Exception("Database lock/crash")):
        with pytest.raises(UploadServiceError):
            service.backend_mediated_upload(
                user=user,
                fileobj=io.BytesIO(b"Data that should not orphan"),
                original_filename='orphan_test.txt',
                content_type='text/plain',
                file_size=27
            )

def test_missing_object_in_storage_marks_session_failed(fail_setup):
    storage = fail_setup['storage']
    user = fail_setup['user']
    service = UploadService(storage)

    init_res = service.init_direct_upload(
        user=user,
        original_filename='missing.bin',
        content_type='application/octet-stream',
        expected_size=1024
    )
    upload_id = init_res['upload_id']

    with pytest.raises(UploadServiceError, match="Verification failed"):
        service.complete_direct_upload(upload_id, user)

    session = UploadSession.objects.get(id=upload_id)
    assert session.status == FileStatus.FAILED
    assert "Verification failed" in session.error_message

def test_expired_session_rejected(fail_setup):
    storage = fail_setup['storage']
    user = fail_setup['user']
    service = UploadService(storage)

    init_res = service.init_direct_upload(
        user=user,
        original_filename='expired.bin',
        content_type='application/octet-stream',
        expected_size=500
    )
    upload_id = init_res['upload_id']
    session = UploadSession.objects.get(id=upload_id)
    session.expires_at = timezone.now() - timedelta(minutes=10)
    session.save()

    with pytest.raises(UploadServiceError, match="Upload session has expired"):
        service.complete_direct_upload(upload_id, user)

def test_simultaneous_completion_idempotency(fail_setup):
    """
    Tests that duplicate or simultaneous completion requests on the same session
    both safely succeed and return the verified StoredFile without race-condition errors.
    """
    storage = fail_setup['storage']
    user = fail_setup['user']
    service = UploadService(storage)

    init_res = service.init_direct_upload(
        user=user,
        original_filename='concurrency.txt',
        content_type='text/plain',
        expected_size=12
    )
    upload_id = init_res['upload_id']
    session = UploadSession.objects.get(id=upload_id)

    # Upload exact object to S3
    storage.put_object_stream(session.file.object_key, io.BytesIO(b"Hello World!"), 'text/plain')

    # First completion
    res1 = service.complete_direct_upload(upload_id, user)
    # Second immediate completion
    res2 = service.complete_direct_upload(upload_id, user)

    assert res1.id == res2.id
    assert res1.status == FileStatus.COMPLETED
    assert res2.status == FileStatus.COMPLETED

def test_multipart_incorrect_etags_rejected(fail_setup):
    storage = fail_setup['storage']
    user = fail_setup['user']
    service = MultipartService(storage)

    session = service.initiate_multipart_session(
        user=user,
        original_filename='test_bad_etags.bin',
        content_type='application/octet-stream',
        expected_size=15 * 1024 * 1024
    )

    # Attempt to complete with bogus ETags
    with pytest.raises(MultipartServiceError):
        service.complete_multipart_session(
            session_id=str(session.id),
            user=user,
            client_parts=[
                {'part_number': 1, 'etag': 'invalid_etag_1'},
                {'part_number': 2, 'etag': 'invalid_etag_2'},
            ]
        )
