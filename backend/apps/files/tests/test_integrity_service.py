import io
import pytest
from apps.files.services.integrity_service import IntegrityService, IntegrityVerificationError

def test_is_multipart_etag():
    # Multipart ETags end with -<part_count>
    assert IntegrityService.is_multipart_etag("d41d8cd98f00b204e9800998ecf8427e-1")
    assert IntegrityService.is_multipart_etag('"d41d8cd98f00b204e9800998ecf8427e-45"')
    # Single part ETags do not have hyphen part count
    assert not IntegrityService.is_multipart_etag("d41d8cd98f00b204e9800998ecf8427e")
    assert not IntegrityService.is_multipart_etag('"d41d8cd98f00b204e9800998ecf8427e"')

def test_verify_object_metadata_success():
    head_data = {
        'content_length': 1024,
        'content_type': 'application/pdf; charset=utf-8',
        'etag': 'abcdef1234567890abcdef1234567890'
    }
    assert IntegrityService.verify_object_metadata(
        head_data=head_data,
        expected_size=1024,
        expected_content_type='application/pdf'
    )

def test_verify_object_metadata_size_mismatch():
    head_data = {'content_length': 500, 'content_type': 'image/png'}
    with pytest.raises(IntegrityVerificationError, match="File size mismatch"):
        IntegrityService.verify_object_metadata(head_data=head_data, expected_size=1024)

def test_verify_object_metadata_content_type_mismatch():
    head_data = {'content_length': 100, 'content_type': 'text/plain'}
    with pytest.raises(IntegrityVerificationError, match="Content-Type mismatch"):
        IntegrityService.verify_object_metadata(
            head_data=head_data,
            expected_size=100,
            expected_content_type='application/pdf'
        )

def test_compute_stream_sha256():
    data = b"Hello Antigravity Object Storage"
    stream = io.BytesIO(data)
    digest = IntegrityService.compute_stream_sha256(stream)
    # Ensure stream position is preserved after hash calculation
    assert stream.tell() == 0
    import hashlib
    assert digest == hashlib.sha256(data).hexdigest()
