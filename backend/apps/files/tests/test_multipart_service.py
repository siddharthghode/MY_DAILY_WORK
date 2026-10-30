import io
import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from apps.files.models import StoredFile, UploadSession, UploadedPart, FileStatus, UploadMode
from apps.files.services.s3_service import S3StorageService
from apps.files.services.multipart_service import MultipartService, MultipartServiceError

@pytest.fixture
def mp_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')
        user = User.objects.create_user(username='bob', password='password123')
        yield {'storage': storage, 'user': user}

def test_part_geometry_calculations():
    # 50 MB with 10 MB default -> 5 parts of 10 MB
    part_size, total_parts = MultipartService.calculate_part_geometry(50 * 1024 * 1024)
    assert part_size == 10 * 1024 * 1024
    assert total_parts == 5

    # 100 GB -> must not exceed 10,000 parts
    part_size, total_parts = MultipartService.calculate_part_geometry(100 * 1024 * 1024 * 1024)
    assert total_parts <= 10000
    assert part_size >= 5 * 1024 * 1024

def test_multipart_lifecycle_complete_and_idempotency(mp_setup):
    storage = mp_setup['storage']
    user = mp_setup['user']
    service = MultipartService(storage)

    file_size = 15 * 1024 * 1024  # 15 MB -> 2 parts (10MB and 5MB)
    session = service.initiate_multipart_session(
        user=user,
        original_filename='large_archive.tar.gz',
        content_type='application/gzip',
        expected_size=file_size
    )

    assert session.upload_mode == UploadMode.DIRECT_MULTIPART
    assert session.total_parts == 2
    assert session.provider_upload_id is not None

    # Generate part URLs
    urls = service.generate_part_urls(session, start_part=1, count=10)
    assert len(urls) == 2
    assert urls[0]['part_number'] == 1
    assert urls[1]['part_number'] == 2

    # Simulate client uploading the 2 parts to S3
    part1_data = b"A" * (10 * 1024 * 1024)
    part2_data = b"B" * (5 * 1024 * 1024)

    res1 = storage.client.upload_part(
        Bucket=storage.bucket_name,
        Key=session.file.object_key,
        UploadId=session.provider_upload_id,
        PartNumber=1,
        Body=part1_data
    )
    res2 = storage.client.upload_part(
        Bucket=storage.bucket_name,
        Key=session.file.object_key,
        UploadId=session.provider_upload_id,
        PartNumber=2,
        Body=part2_data
    )

    # Record parts in database
    service.record_uploaded_parts(session, [
        {'part_number': 1, 'etag': res1['ETag']},
        {'part_number': 2, 'etag': res2['ETag']}
    ])

    # Complete session
    completed_file = service.complete_multipart_session(str(session.id), user)
    assert completed_file.status == FileStatus.COMPLETED
    assert completed_file.verified_size == file_size

    # Verify idempotency
    repeated_file = service.complete_multipart_session(str(session.id), user)
    assert repeated_file.id == completed_file.id

def test_multipart_missing_parts(mp_setup):
    storage = mp_setup['storage']
    user = mp_setup['user']
    service = MultipartService(storage)

    session = service.initiate_multipart_session(
        user=user,
        original_filename='video.mp4',
        content_type='video/mp4',
        expected_size=20 * 1024 * 1024  # 2 parts
    )

    # Upload only part 1
    res1 = storage.client.upload_part(
        Bucket=storage.bucket_name,
        Key=session.file.object_key,
        UploadId=session.provider_upload_id,
        PartNumber=1,
        Body=b"A" * (10 * 1024 * 1024)
    )
    service.record_uploaded_parts(session, [{'part_number': 1, 'etag': res1['ETag']}])

    # Complete without part 2 -> should fail
    with pytest.raises(MultipartServiceError, match="parts are missing"):
        service.complete_multipart_session(str(session.id), user)

def test_multipart_abort(mp_setup):
    storage = mp_setup['storage']
    user = mp_setup['user']
    service = MultipartService(storage)

    session = service.initiate_multipart_session(
        user=user,
        original_filename='unwanted.iso',
        content_type='application/octet-stream',
        expected_size=10 * 1024 * 1024
    )

    service.abort_multipart_session(str(session.id), user)
    session.refresh_from_db()
    assert session.status == FileStatus.ABORTED
    assert session.file.status == FileStatus.ABORTED
