import io
import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from django.db import IntegrityError
from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from apps.files.services.s3_service import S3StorageService
from apps.files.services.upload_service import UploadService, UploadServiceError

@pytest.fixture
def test_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')
        user = User.objects.create_user(username='alice', password='password123')
        yield {'storage': storage, 'user': user}

def test_backend_mediated_upload_success(test_setup):
    storage = test_setup['storage']
    user = test_setup['user']
    service = UploadService(storage)

    content = b"Small file payload for backend streaming"
    stream = io.BytesIO(content)

    file_obj = service.backend_mediated_upload(
        user=user,
        fileobj=stream,
        original_filename='notes.txt',
        content_type='text/plain',
        file_size=len(content)
    )

    assert file_obj.status == FileStatus.COMPLETED
    assert file_obj.verified_size == len(content)
    assert file_obj.original_filename == 'notes.txt'
    assert file_obj.owner == user

    # S3 verification
    head = storage.head_object(file_obj.object_key)
    assert head['content_length'] == len(content)

def test_backend_mediated_upload_oversized(test_setup, settings):
    storage = test_setup['storage']
    user = test_setup['user']
    settings.BACKEND_MEDIATED_MAX_BYTES = 100
    service = UploadService(storage)

    stream = io.BytesIO(b"A" * 200)
    with pytest.raises(UploadServiceError, match="exceeds backend-mediated limit"):
        service.backend_mediated_upload(
            user=user,
            fileobj=stream,
            original_filename='large.bin',
            content_type='application/octet-stream',
            file_size=200
        )

def test_init_direct_upload(test_setup):
    storage = test_setup['storage']
    user = test_setup['user']
    service = UploadService(storage)

    res = service.init_direct_upload(
        user=user,
        original_filename='dataset.csv',
        content_type='text/csv',
        expected_size=50000,
        use_post_policy=True
    )

    assert 'upload_id' in res
    assert 'post_url' in res
    assert 'post_fields' in res
    assert res['upload_method'] == 'POST'

    session = UploadSession.objects.get(id=res['upload_id'])
    assert session.status == FileStatus.UPLOADING
    assert session.file.status == FileStatus.UPLOADING

def test_complete_direct_upload_success_and_idempotency(test_setup):
    storage = test_setup['storage']
    user = test_setup['user']
    service = UploadService(storage)

    init_res = service.init_direct_upload(
        user=user,
        original_filename='photo.jpg',
        content_type='image/jpeg',
        expected_size=100
    )
    upload_id = init_res['upload_id']
    session = UploadSession.objects.get(id=upload_id)

    # Simulate client uploading the exact 100 bytes to S3
    storage.put_object_stream(
        object_key=session.file.object_key,
        fileobj=io.BytesIO(b"X" * 100),
        content_type='image/jpeg'
    )

    # Call complete
    completed_file = service.complete_direct_upload(session_id=upload_id, user=user)
    assert completed_file.status == FileStatus.COMPLETED
    assert completed_file.verified_size == 100

    # Idempotent second call: must succeed without throwing error
    repeat_file = service.complete_direct_upload(session_id=upload_id, user=user)
    assert repeat_file.id == completed_file.id

def test_complete_direct_upload_missing_object(test_setup):
    storage = test_setup['storage']
    user = test_setup['user']
    service = UploadService(storage)

    init_res = service.init_direct_upload(
        user=user,
        original_filename='ghost.bin',
        content_type='application/octet-stream',
        expected_size=200
    )
    upload_id = init_res['upload_id']

    # Do NOT upload to S3, call complete
    with pytest.raises(UploadServiceError, match="Verification failed: object was not uploaded"):
        service.complete_direct_upload(session_id=upload_id, user=user)

    session = UploadSession.objects.get(id=upload_id)
    assert session.status == FileStatus.FAILED
