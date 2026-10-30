import io
from datetime import timedelta
import pytest
import boto3
from moto import mock_aws
from django.utils import timezone
from django.contrib.auth.models import User
from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from apps.files.services.s3_service import S3StorageService
from apps.files.services.cleanup_service import CleanupService

@pytest.fixture
def cleanup_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')
        user = User.objects.create_user(username='admin_cleaner', password='password123')
        yield {'storage': storage, 'user': user}

def test_expire_stale_sessions(cleanup_setup):
    storage = cleanup_setup['storage']
    user = cleanup_setup['user']
    service = CleanupService(storage)

    past = timezone.now() - timedelta(hours=2)
    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/files/stale.txt',
        bucket_name='test-bucket',
        original_filename='stale.txt',
        content_type='text/plain',
        expected_size=100,
        status=FileStatus.UPLOADING,
        expired_at=past
    )
    session = UploadSession.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        file=file_obj,
        upload_mode=UploadMode.DIRECT_SINGLE,
        expected_size=100,
        expected_content_type='text/plain',
        status=FileStatus.UPLOADING,
        expires_at=past
    )

    expired_count = service.expire_stale_sessions()
    assert expired_count == 1

    session.refresh_from_db()
    file_obj.refresh_from_db()
    assert session.status == FileStatus.EXPIRED
    assert file_obj.status == FileStatus.EXPIRED

def test_abort_stale_multipart_uploads(cleanup_setup):
    storage = cleanup_setup['storage']
    user = cleanup_setup['user']
    service = CleanupService(storage)

    object_key = 'tenants/files/stale_multipart.bin'
    upload_id = storage.initiate_multipart_upload(object_key, 'application/octet-stream')

    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key=object_key,
        bucket_name='test-bucket',
        original_filename='stale_multipart.bin',
        content_type='application/octet-stream',
        expected_size=10485760,
        status=FileStatus.ABORTED
    )
    session = UploadSession.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        file=file_obj,
        upload_mode=UploadMode.DIRECT_MULTIPART,
        provider_upload_id=upload_id,
        expected_size=10485760,
        expected_content_type='application/octet-stream',
        status=FileStatus.ABORTED,
        expires_at=timezone.now()
    )

    aborted_count = service.abort_stale_multipart_uploads()
    assert aborted_count == 1
    session.refresh_from_db()
    assert session.provider_upload_id is None

def test_reconciliation_never_deletes_completed_files(cleanup_setup):
    storage = cleanup_setup['storage']
    user = cleanup_setup['user']
    service = CleanupService(storage)

    # Completed file
    completed = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/files/important_invoice.pdf',
        bucket_name='test-bucket',
        original_filename='important_invoice.pdf',
        content_type='application/pdf',
        expected_size=500,
        verified_size=500,
        status=FileStatus.COMPLETED
    )

    # Verifying file whose object actually exists in S3
    reconciled_file = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/files/verifying.pdf',
        bucket_name='test-bucket',
        original_filename='verifying.pdf',
        content_type='application/pdf',
        expected_size=10,
        status=FileStatus.VERIFYING
    )
    storage.put_object_stream('tenants/files/verifying.pdf', io.BytesIO(b"0123456789"), 'application/pdf')

    res = service.reconcile_pending_files()
    assert res['reconciled'] == 1

    completed.refresh_from_db()
    assert completed.status == FileStatus.COMPLETED
    reconciled_file.refresh_from_db()
    assert reconciled_file.status == FileStatus.COMPLETED
