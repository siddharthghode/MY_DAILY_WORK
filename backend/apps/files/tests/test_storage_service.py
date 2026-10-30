import io
import pytest
import boto3
from moto import mock_aws
from apps.files.services.s3_service import S3StorageService, S3PreconditionFailedError

@pytest.fixture
def s3_service():
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        service = S3StorageService(
            bucket_name='test-bucket',
            region_name='us-east-1',
            access_key='mock-key',
            secret_key='mock-secret'
        )
        yield service

def test_presigned_put_url_generation(s3_service):
    url = s3_service.generate_presigned_put_url(
        object_key='sample/test.txt',
        content_type='text/plain',
        expires_in=600
    )
    assert "sample/test.txt" in url
    assert "X-Amz-Signature" in url

def test_presigned_post_policy_generation(s3_service):
    post_data = s3_service.generate_presigned_post_policy(
        object_key='sample/test.png',
        content_type='image/png',
        min_size=1,
        max_size=1048576,
        expires_in=300
    )
    assert 'url' in post_data
    assert 'fields' in post_data
    assert post_data['fields']['key'] == 'sample/test.png'
    assert post_data['fields']['Content-Type'] == 'image/png'

def test_put_object_stream_and_head(s3_service):
    data = b"Testing S3 stream streaming contents"
    stream = io.BytesIO(data)
    result = s3_service.put_object_stream(
        object_key='streamed/data.txt',
        fileobj=stream,
        content_type='text/plain',
        content_length=len(data)
    )
    assert 'etag' in result

    head = s3_service.head_object('streamed/data.txt')
    assert head is not None
    assert head['content_length'] == len(data)
    assert head['content_type'] == 'text/plain'

def test_head_missing_object(s3_service):
    assert s3_service.head_object('non_existent.txt') is None

def test_presigned_get_url(s3_service):
    url = s3_service.generate_presigned_get_url(
        object_key='reports/annual.pdf',
        expires_in=900,
        filename_override='annual_report_2026.pdf',
        response_content_type='application/pdf'
    )
    assert "reports/annual.pdf" in url
    assert "response-content-disposition" in url or "ResponseContentDisposition" in url or "X-Amz-Signature" in url

def test_delete_object(s3_service):
    s3_service.put_object_stream(
        object_key='to_delete.txt',
        fileobj=io.BytesIO(b"data"),
        content_type='text/plain'
    )
    assert s3_service.head_object('to_delete.txt') is not None
    assert s3_service.delete_object('to_delete.txt') is True
    assert s3_service.head_object('to_delete.txt') is None

def test_multipart_lifecycle(s3_service):
    object_key = 'multipart/big_data.bin'
    upload_id = s3_service.initiate_multipart_upload(
        object_key=object_key,
        content_type='application/octet-stream'
    )
    assert upload_id is not None

    part_url = s3_service.generate_presigned_part_url(
        object_key=object_key,
        upload_id=upload_id,
        part_number=1
    )
    assert f"partNumber=1" in part_url or f"partNumber=1".lower() in part_url.lower()

    # Upload 2 chunks using mock s3 client directly
    part1_data = b"A" * 5242880  # 5MB
    part2_data = b"B" * 5242880  # 5MB
    res1 = s3_service.client.upload_part(
        Bucket=s3_service.bucket_name,
        Key=object_key,
        UploadId=upload_id,
        PartNumber=1,
        Body=part1_data
    )
    res2 = s3_service.client.upload_part(
        Bucket=s3_service.bucket_name,
        Key=object_key,
        UploadId=upload_id,
        PartNumber=2,
        Body=part2_data
    )

    parts_list = s3_service.list_parts(object_key, upload_id)
    assert len(parts_list) == 2
    assert parts_list[0]['PartNumber'] == 1
    assert parts_list[1]['PartNumber'] == 2

    # Complete multipart upload
    comp_res = s3_service.complete_multipart_upload(
        object_key=object_key,
        upload_id=upload_id,
        parts=[
            {'PartNumber': 1, 'ETag': res1['ETag']},
            {'PartNumber': 2, 'ETag': res2['ETag']}
        ]
    )
    assert comp_res is not None

    head = s3_service.head_object(object_key)
    assert head['content_length'] == len(part1_data) + len(part2_data)

def test_abort_multipart_upload(s3_service):
    object_key = 'abandoned/file.bin'
    upload_id = s3_service.initiate_multipart_upload(
        object_key=object_key,
        content_type='application/octet-stream'
    )
    s3_service.abort_multipart_upload(object_key, upload_id)
    # After abort, listing parts will raise or return empty
    with pytest.raises(Exception):
        s3_service.list_parts(object_key, upload_id)
