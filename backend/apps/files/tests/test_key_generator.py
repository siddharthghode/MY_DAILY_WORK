import uuid
import pytest
from apps.files.services.key_generator import ObjectKeyGenerator

def test_sanitize_filename_traversal():
    dirty = "../../../../../etc/passwd"
    clean = ObjectKeyGenerator.sanitize_filename(dirty)
    assert clean == "passwd"
    assert ".." not in clean
    assert "/" not in clean

def test_sanitize_filename_special_chars_and_nulls():
    dirty = "test\x00file*name?<>.png"
    clean = ObjectKeyGenerator.sanitize_filename(dirty)
    assert "\x00" not in clean
    assert clean == "testfile_name___.png"



def test_sanitize_filename_empty_or_dots():
    assert ObjectKeyGenerator.sanitize_filename("") == "unnamed_file"
    assert ObjectKeyGenerator.sanitize_filename("...") == "file"
    assert ObjectKeyGenerator.sanitize_filename(".hidden") == "hidden"

def test_generate_tenant_key():
    file_id = uuid.uuid4()
    key = ObjectKeyGenerator.generate_tenant_key(
        tenant_id="acme_corp",
        file_id=file_id,
        original_filename="financial_report.pdf",
        is_public=False
    )
    assert key.startswith("tenants/acme_corp/files/")
    assert str(file_id) in key
    assert key.endswith("financial_report.pdf")

def test_generate_public_key():
    file_id = uuid.uuid4()
    key = ObjectKeyGenerator.generate_tenant_key(
        tenant_id="acme_corp",
        file_id=file_id,
        original_filename="logo.svg",
        is_public=True
    )
    assert key.startswith("public/files/")
    assert str(file_id) in key
    assert key.endswith("logo.svg")

def test_generate_content_addressed_key():
    sample_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    key = ObjectKeyGenerator.generate_content_addressed_key(sample_hash, "empty.txt")
    assert key == "cas/e3/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855/empty.txt"

def test_generate_content_addressed_key_invalid_hash():
    with pytest.raises(ValueError):
        ObjectKeyGenerator.generate_content_addressed_key("short_hash", "file.txt")
