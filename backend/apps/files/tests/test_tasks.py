import pytest
import boto3
from moto import mock_aws
from django.contrib.auth.models import User
from apps.files.models import StoredFile, FileStatus
from apps.files.tasks import process_video_transcoding, cleanup_stale_sessions_task, reconcile_storage_task

from unittest.mock import patch
import subprocess

@pytest.fixture
def task_setup(db):
    with mock_aws():
        client = boto3.client('s3', region_name='us-east-1')
        client.create_bucket(Bucket='test-bucket')
        user = User.objects.create_user(username='task_user', password='password123')
        yield {'user': user}

def fake_ffmpeg_run(cmd, *args, **kwargs):
    # Output file is the last argument
    output_path = cmd[-1]
    with open(output_path, 'wb') as f:
        f.write(b"MOCK_MP4_PREVIEW_BYTES")
    return subprocess.CompletedProcess(args=cmd, returncode=0)

def test_process_video_transcoding_task(task_setup):
    user = task_setup['user']
    file_obj = StoredFile.objects.create(
        owner=user,
        tenant_id=user.profile.tenant_id,
        object_key='tenants/video/sample.mp4',
        bucket_name='test-bucket',
        original_filename='sample.mp4',
        content_type='video/mp4',
        expected_size=1024,
        verified_size=1024,
        status=FileStatus.COMPLETED
    )

    with patch('subprocess.run', side_effect=fake_ffmpeg_run):
        process_video_transcoding(str(file_obj.id))

    file_obj.refresh_from_db()
    assert 'renditions' in file_obj.metadata
    assert 'preview_key' in file_obj.metadata['renditions']


def test_periodic_cleanup_and_reconcile_tasks(task_setup):
    clean_res = cleanup_stale_sessions_task()
    assert 'expired_sessions' in clean_res
    assert 'aborted_multipart' in clean_res

    rec_res = reconcile_storage_task()
    assert 'reconciled' in rec_res
    assert 'failed' in rec_res
