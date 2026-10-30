from django.urls import path
from apps.files.views import (
    UploadInitView,
    UploadSessionDetailView,
    UploadPartUrlsView,
    UploadCompleteView,
    UploadAbortView,
    UploadResumeView,
    FileListView,
    FileDetailView,
    FileDownloadUrlView,
    FileStatusView,
)

app_name = 'files'

urlpatterns = [
    # Upload lifecycle endpoints
    path('uploads/init/', UploadInitView.as_view(), name='upload_init'),
    path('uploads/<uuid:upload_id>/', UploadSessionDetailView.as_view(), name='upload_detail'),
    path('uploads/<uuid:upload_id>/parts/urls/', UploadPartUrlsView.as_view(), name='upload_part_urls'),
    path('uploads/<uuid:upload_id>/complete/', UploadCompleteView.as_view(), name='upload_complete'),
    path('uploads/<uuid:upload_id>/abort/', UploadAbortView.as_view(), name='upload_abort'),
    path('uploads/<uuid:upload_id>/resume/', UploadResumeView.as_view(), name='upload_resume'),

    # File registry and management endpoints
    path('', FileListView.as_view(), name='file_list'),
    path('<uuid:file_id>/', FileDetailView.as_view(), name='file_detail'),
    path('<uuid:file_id>/download-url/', FileDownloadUrlView.as_view(), name='file_download_url'),
    path('<uuid:file_id>/status/', FileStatusView.as_view(), name='file_status'),
]
