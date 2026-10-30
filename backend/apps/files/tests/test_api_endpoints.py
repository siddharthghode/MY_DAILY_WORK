import io
import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from apps.files.models import StoredFile, UploadSession, FileStatus, UploadMode
from apps.files.services.s3_service import S3StorageService

@pytest.fixture
def api_setup(db):
    with mock_aws():
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.create_bucket(Bucket='test-bucket')
        storage = S3StorageService(bucket_name='test-bucket', region_name='us-east-1')

        alice = User.objects.create_user(username='alice', password='password123')
        bob = User.objects.create_user(username='bob', password='password123')

        client_alice = APIClient()
        client_alice.force_authenticate(user=alice)

        client_bob = APIClient()
        client_bob.force_authenticate(user=bob)

        client_anon = APIClient()

        yield {
            'storage': storage,
            'alice': alice,
            'bob': bob,
            'client_alice': client_alice,
            'client_bob': client_bob,
            'client_anon': client_anon,
        }

def test_unauthenticated_requests_rejected(api_setup):
    anon = api_setup['client_anon']
    assert anon.get('/api/files/').status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)
    assert anon.post('/api/files/uploads/init/', {}).status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)

def test_upload_init_backend_mediated(api_setup):
    client = api_setup['client_alice']
    file_content = b"Backend uploaded file contents"
    uploaded = io.BytesIO(file_content)
    uploaded.name = 'sample.txt'

    response = client.post('/api/files/uploads/init/', {
        'original_filename': 'sample.txt',
        'content_type': 'text/plain',
        'file_size': len(file_content),
        'upload_mode': UploadMode.BACKEND_MEDIATED,
        'file': uploaded
    }, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['status'] == FileStatus.COMPLETED
    assert data['verified_size'] == len(file_content)

def test_upload_init_direct_single(api_setup):
    client = api_setup['client_alice']
    response = client.post('/api/files/uploads/init/', {
        'original_filename': 'photo.png',
        'content_type': 'image/png',
        'file_size': 2048,
        'upload_mode': UploadMode.DIRECT_SINGLE,
        'use_post_policy': True
    }, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert 'upload_id' in data
    assert 'post_url' in data
    assert 'post_fields' in data

def test_upload_init_direct_multipart(api_setup):
    client = api_setup['client_alice']
    response = client.post('/api/files/uploads/init/', {
        'original_filename': 'large_movie.mp4',
        'content_type': 'video/mp4',
        'file_size': 30 * 1024 * 1024,
        'upload_mode': UploadMode.DIRECT_MULTIPART
    }, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert 'upload_id' in data
    assert data['total_parts'] == 3
    assert data['part_size'] == 10 * 1024 * 1024

def test_idor_cross_user_session_access_denied(api_setup):
    alice_client = api_setup['client_alice']
    bob_client = api_setup['client_bob']

    # Alice initializes an upload
    init_res = alice_client.post('/api/files/uploads/init/', {
        'original_filename': 'alice_secret.pdf',
        'content_type': 'application/pdf',
        'file_size': 500,
        'upload_mode': UploadMode.DIRECT_SINGLE
    }, format='json')
    upload_id = init_res.json()['upload_id']

    # Bob tries to access Alice's session
    bob_res = bob_client.get(f'/api/files/uploads/{upload_id}/')
    assert bob_res.status_code == status.HTTP_404_NOT_FOUND

def test_file_listing_and_pagination(api_setup):
    client = api_setup['client_alice']
    user = api_setup['alice']

    for i in range(5):
        StoredFile.objects.create(
            owner=user,
            tenant_id=user.profile.tenant_id,
            object_key=f'tenants/alice/file_{i}.txt',
            bucket_name='test-bucket',
            original_filename=f'file_{i}.txt',
            content_type='text/plain',
            expected_size=100,
            status=FileStatus.COMPLETED
        )

    res = client.get('/api/files/?search=file_')
    assert res.status_code == status.HTTP_200_OK
    assert res.json()['count'] == 5

def test_download_url_generation_api(api_setup):
    client = api_setup['client_alice']
    user = api_setup['alice']

    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/alice/files/download_test.txt',
        bucket_name='test-bucket',
        original_filename='download_test.txt',
        content_type='text/plain',
        expected_size=100,
        verified_size=100,
        status=FileStatus.COMPLETED
    )

    res = client.post(f'/api/files/{file_obj.id}/download-url/', {
        'expires_in': 600,
        'as_attachment': True
    }, format='json')

    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert 'url' in data
    assert data['delivery_method'] == 'PRESIGNED_S3'
    assert data['supports_ranges'] is True

def test_file_delete_deletes_s3_object(api_setup):
    client = api_setup['client_alice']
    storage = api_setup['storage']
    user = api_setup['alice']

    # Create file in storage and DB
    key = 'tenants/alice/to_be_deleted.txt'
    storage.put_object_stream(key, io.BytesIO(b"Data"), 'text/plain')
    assert storage.head_object(key) is not None

    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key=key,
        bucket_name='test-bucket',
        original_filename='to_be_deleted.txt',
        content_type='text/plain',
        expected_size=4,
        verified_size=4,
        status=FileStatus.COMPLETED
    )

    del_res = client.delete(f'/api/files/{file_obj.id}/')
    assert del_res.status_code == status.HTTP_204_NO_CONTENT
    assert not StoredFile.objects.filter(id=file_obj.id).exists()
    assert storage.head_object(key) is None

def test_file_status_endpoint(api_setup):
    client = api_setup['client_alice']
    user = api_setup['alice']

    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/alice/files/status_test.bin',
        bucket_name='test-bucket',
        original_filename='status_test.bin',
        content_type='application/octet-stream',
        expected_size=512,
        status=FileStatus.UPLOADING
    )

    res = client.get(f'/api/files/{file_obj.id}/status/')
    assert res.status_code == status.HTTP_200_OK
    assert res.json()['status'] == FileStatus.UPLOADING
