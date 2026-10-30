from rest_framework import serializers
from apps.files.models import StoredFile, UploadSession, UploadedPart, FileStatus, UploadMode

class StoredFileSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = StoredFile
        fields = [
            'id',
            'owner_username',
            'tenant_id',
            'original_filename',
            'content_type',
            'expected_size',
            'verified_size',
            'etag',
            'checksum',
            'status',
            'is_public',
            'metadata',
            'created_at',
            'updated_at',
            'completed_at',
        ]
        read_only_fields = fields

class StoredFileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoredFile
        fields = ['id', 'status', 'expected_size', 'verified_size', 'completed_at']
        read_only_fields = fields

class UploadedPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedPart
        fields = ['part_number', 'etag', 'size', 'checksum', 'uploaded_at']

class UploadSessionDetailSerializer(serializers.ModelSerializer):
    file = StoredFileSerializer(read_only=True)
    parts = UploadedPartSerializer(many=True, read_only=True)

    class Meta:
        model = UploadSession
        fields = [
            'id',
            'upload_mode',
            'status',
            'expected_size',
            'expected_content_type',
            'part_size',
            'total_parts',
            'error_message',
            'expires_at',
            'created_at',
            'file',
            'parts',
        ]
        read_only_fields = fields

class UploadInitSerializer(serializers.Serializer):
    original_filename = serializers.CharField(max_length=255)
    content_type = serializers.CharField(max_length=128)
    file_size = serializers.IntegerField(min_value=1)
    upload_mode = serializers.ChoiceField(
        choices=UploadMode.choices,
        default=UploadMode.DIRECT_SINGLE
    )
    is_public = serializers.BooleanField(default=False)
    use_post_policy = serializers.BooleanField(default=True)
    metadata = serializers.DictField(required=False, default=dict)
    file = serializers.FileField(required=False)

    def validate(self, attrs):
        mode = attrs.get('upload_mode')
        file = attrs.get('file')
        if mode == UploadMode.BACKEND_MEDIATED and not file:
            raise serializers.ValidationError({"file": "File is required for backend-mediated uploads."})
        return attrs

class PartUrlsRequestSerializer(serializers.Serializer):
    start_part = serializers.IntegerField(min_value=1, default=1)
    count = serializers.IntegerField(min_value=1, max_value=50, default=10)

class PartItemSerializer(serializers.Serializer):
    part_number = serializers.IntegerField(min_value=1)
    etag = serializers.CharField(max_length=128)
    size = serializers.IntegerField(required=False)

class UploadCompleteSerializer(serializers.Serializer):
    parts = serializers.ListField(
        child=PartItemSerializer(),
        required=False,
        default=list
    )
    checksum = serializers.CharField(max_length=128, required=False, allow_blank=True)

class DownloadUrlRequestSerializer(serializers.Serializer):
    expires_in = serializers.IntegerField(min_value=60, max_value=86400, default=900)
    as_attachment = serializers.BooleanField(default=True)
