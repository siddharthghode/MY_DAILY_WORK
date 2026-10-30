import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from apps.files.models import StoredFile, FileStatus
from apps.files.services.s3_service import S3StorageService
from apps.files.services.download_service import DownloadService, DownloadServiceError

@pytest.fixture
def dl_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')
        alice = User.objects.create_user(username='alice', password='password123')
        charlie = User.objects.create_user(username='charlie', password='password123')
        yield {'storage': storage, 'alice': alice, 'charlie': charlie}

def test_download_private_file_owner_success(dl_setup):
    storage = dl_setup['storage']
    alice = dl_setup['alice']
    service = DownloadService(storage)

    file_obj = StoredFile.objects.create(
        owner=alice,
        tenant_id=alice.profile.tenant_id,
        object_key='tenants/alice/files/doc.pdf',
        bucket_name='test-bucket',
        original_filename='doc.pdf',
        content_type='application/pdf',
        expected_size=1024,
        verified_size=1024,
        status=FileStatus.COMPLETED
    )

    res = service.get_download_url(file_obj, alice)
    assert res['delivery_method'] == 'PRESIGNED_S3'
    assert 'url' in res
    assert res['supports_ranges'] is True
    assert res['filename'] == 'doc.pdf'

def test_download_private_file_cross_user_denied(dl_setup):
    storage = dl_setup['storage']
    alice = dl_setup['alice']
    charlie = dl_setup['charlie']
    service = DownloadService(storage)

    file_obj = StoredFile.objects.create(
        owner=alice,
        tenant_id='tenant_alice',
        object_key='tenants/alice/files/secret.docx',
        bucket_name='test-bucket',
        original_filename='secret.docx',
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        expected_size=2048,
        status=FileStatus.COMPLETED
    )

    with pytest.raises(DownloadServiceError, match="Access denied"):
        service.get_download_url(file_obj, charlie)

def test_download_public_file_with_cdn(dl_setup, settings):
    storage = dl_setup['storage']
    alice = dl_setup['alice']
    settings.CDN_BASE_URL = 'https://cdn.mycompany.com'
    service = DownloadService(storage)

    file_obj = StoredFile.objects.create(
        owner=alice,
        tenant_id='tenant_alice',
        object_key='public/files/brand_logo.svg',
        bucket_name='test-bucket',
        original_filename='brand_logo.svg',
        content_type='image/svg+xml',
        expected_size=512,
        status=FileStatus.COMPLETED,
        is_public=True
    )

    res = service.get_download_url(file_obj, None)
    assert res['delivery_method'] == 'CDN'
    assert res['url'] == 'https://cdn.mycompany.com/public/files/brand_logo.svg'

def test_download_incomplete_file_rejected(dl_setup):
    storage = dl_setup['storage']
    alice = dl_setup['alice']
    service = DownloadService(storage)

    file_obj = StoredFile.objects.create(
        owner=alice,
        tenant_id=alice.profile.tenant_id,
        object_key='tenants/alice/files/pending.bin',
        bucket_name='test-bucket',
        original_filename='pending.bin',
        content_type='application/octet-stream',
        expected_size=100,
        status=FileStatus.UPLOADING
    )

    with pytest.raises(DownloadServiceError, match="File is not available for download"):
        service.get_download_url(file_obj, alice)
