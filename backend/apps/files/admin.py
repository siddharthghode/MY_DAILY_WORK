from django.contrib import admin
from apps.files.models import StoredFile, UploadSession, UploadedPart

class UploadedPartInline(admin.TabularInline):
    model = UploadedPart
    extra = 0
    readonly_fields = ('part_number', 'etag', 'size', 'checksum', 'uploaded_at')

@admin.register(StoredFile)
class StoredFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_filename', 'owner', 'tenant_id', 'status', 'expected_size', 'verified_size', 'created_at')
    list_filter = ('status', 'is_public', 'storage_provider', 'created_at')
    search_fields = ('original_filename', 'object_key', 'tenant_id', 'owner__username')
    readonly_fields = ('id', 'created_at', 'updated_at', 'completed_at', 'expired_at')

@admin.register(UploadSession)
class UploadSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'upload_mode', 'status', 'total_parts', 'expires_at', 'created_at')
    list_filter = ('upload_mode', 'status', 'created_at')
    search_fields = ('id', 'provider_upload_id', 'owner__username', 'file__object_key')
    readonly_fields = ('id', 'created_at', 'updated_at', 'completed_at')
    inlines = [UploadedPartInline]
