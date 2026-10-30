import logging
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from apps.files.models import StoredFile, UploadSession, UploadMode, FileStatus
from apps.files.serializers import (
    StoredFileSerializer,
    StoredFileStatusSerializer,
    UploadSessionDetailSerializer,
    UploadInitSerializer,
    PartUrlsRequestSerializer,
    UploadCompleteSerializer,
    DownloadUrlRequestSerializer
)
from apps.files.permissions import IsOwnerOrTenantMember
from apps.files.selectors import get_user_files, get_file_by_id, get_upload_session_by_id
from apps.files.services import get_storage_service
from apps.files.services.upload_service import UploadService, UploadServiceError
from apps.files.services.multipart_service import MultipartService, MultipartServiceError
from apps.files.services.download_service import DownloadService, DownloadServiceError

logger = logging.getLogger(__name__)

class UploadInitView(APIView):
    """
    Initializes an upload session:
    - Mode A: Backend-mediated streaming upload (for files < 10MB)
    - Mode B: Direct single pre-signed upload (PUT URL or POST policy)
    - Mode C: Direct multipart upload (for large files up to 5TB)
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=UploadInitSerializer, responses={201: OpenApiTypes.OBJECT})
    def post(self, request):
        serializer = UploadInitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        storage = get_storage_service()
        upload_mode = data['upload_mode']
        user = request.user
        tenant_id = getattr(getattr(user, 'profile', None), 'tenant_id', None)

        try:
            if upload_mode == UploadMode.BACKEND_MEDIATED:
                uploaded_file = data['file']
                upload_service = UploadService(storage)
                stored_file = upload_service.backend_mediated_upload(
                    user=user,
                    fileobj=uploaded_file,
                    original_filename=data['original_filename'],
                    content_type=data['content_type'],
                    file_size=data['file_size'],
                    tenant_id=tenant_id,
                    is_public=data['is_public'],
                    metadata=data.get('metadata')
                )
                return Response(StoredFileSerializer(stored_file).data, status=status.HTTP_201_CREATED)

            elif upload_mode == UploadMode.DIRECT_SINGLE:
                upload_service = UploadService(storage)
                init_data = upload_service.init_direct_upload(
                    user=user,
                    original_filename=data['original_filename'],
                    content_type=data['content_type'],
                    expected_size=data['file_size'],
                    tenant_id=tenant_id,
                    is_public=data['is_public'],
                    use_post_policy=data['use_post_policy'],
                    metadata=data.get('metadata')
                )
                return Response(init_data, status=status.HTTP_201_CREATED)

            elif upload_mode == UploadMode.DIRECT_MULTIPART:
                multipart_service = MultipartService(storage)
                session = multipart_service.initiate_multipart_session(
                    user=user,
                    original_filename=data['original_filename'],
                    content_type=data['content_type'],
                    expected_size=data['file_size'],
                    tenant_id=tenant_id,
                    is_public=data['is_public'],
                    metadata=data.get('metadata')
                )
                return Response({
                    'upload_id': str(session.id),
                    'file_id': str(session.file.id),
                    'object_key': session.file.object_key,
                    'upload_mode': session.upload_mode,
                    'part_size': session.part_size,
                    'total_parts': session.total_parts,
                    'expires_at': session.expires_at.isoformat(),
                }, status=status.HTTP_201_CREATED)

        except (UploadServiceError, MultipartServiceError) as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UploadSessionDetailView(APIView):
    """Retrieves current state and parts list of an upload session."""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses={200: UploadSessionDetailSerializer})
    def get(self, request, upload_id):
        session = get_upload_session_by_id(upload_id, request.user)
        if not session:
            raise NotFound("Upload session not found or unauthorized.")
        return Response(UploadSessionDetailSerializer(session).data)

class UploadPartUrlsView(APIView):
    """Generates a batch of pre-signed PUT URLs for multipart chunk uploads."""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=PartUrlsRequestSerializer, responses={200: OpenApiTypes.OBJECT})
    def post(self, request, upload_id):
        session = get_upload_session_by_id(upload_id, request.user)
        if not session:
            raise NotFound("Upload session not found.")
        if session.upload_mode != UploadMode.DIRECT_MULTIPART:
            raise ValidationError("Session is not a multipart upload.")

        serializer = PartUrlsRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        storage = get_storage_service()
        service = MultipartService(storage)
        try:
            urls = service.generate_part_urls(
                session=session,
                start_part=serializer.validated_data['start_part'],
                count=serializer.validated_data['count']
            )
            return Response({'parts': urls})
        except MultipartServiceError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UploadCompleteView(APIView):
    """
    Completes and verifies an upload session (both direct single and multipart).
    Performs server-side HEAD verification and atomic state transitions.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=UploadCompleteSerializer, responses={200: StoredFileSerializer})
    def post(self, request, upload_id):
        session = get_upload_session_by_id(upload_id, request.user)
        if not session:
            raise NotFound("Upload session not found.")

        serializer = UploadCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        storage = get_storage_service()
        try:
            if session.upload_mode == UploadMode.DIRECT_MULTIPART:
                service = MultipartService(storage)
                stored_file = service.complete_multipart_session(
                    session_id=str(session.id),
                    user=request.user,
                    client_parts=data.get('parts')
                )
            else:
                service = UploadService(storage)
                stored_file = service.complete_direct_upload(
                    session_id=str(session.id),
                    user=request.user,
                    expected_checksum=data.get('checksum')
                )

            return Response(StoredFileSerializer(stored_file).data)
        except (UploadServiceError, MultipartServiceError) as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UploadAbortView(APIView):
    """Aborts an in-progress upload session and purges provider resources."""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: OpenApiTypes.OBJECT}
    )
    def post(self, request, upload_id):
        session = get_upload_session_by_id(upload_id, request.user)
        if not session:
            raise NotFound("Upload session not found.")

        storage = get_storage_service()
        try:
            if session.upload_mode == UploadMode.DIRECT_MULTIPART:
                service = MultipartService(storage)
                service.abort_multipart_session(str(session.id), request.user)
            else:
                session.status = FileStatus.ABORTED
                session.save(update_fields=['status'])
                session.file.status = FileStatus.ABORTED
                session.file.save(update_fields=['status'])
            return Response({'detail': 'Upload session aborted successfully.'})
        except MultipartServiceError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UploadResumeView(APIView):
    """Queries S3 for already uploaded parts to allow client to resume without re-uploading."""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: OpenApiTypes.OBJECT}
    )
    def post(self, request, upload_id):
        session = get_upload_session_by_id(upload_id, request.user)

        if not session:
            raise NotFound("Upload session not found.")
        if session.upload_mode != UploadMode.DIRECT_MULTIPART:
            raise ValidationError("Resume is only applicable to multipart uploads.")

        storage = get_storage_service()
        service = MultipartService(storage)
        try:
            synced_parts = service.sync_parts_from_storage(session)
            return Response({
                'upload_id': str(session.id),
                'total_parts': session.total_parts,
                'part_size': session.part_size,
                'uploaded_parts': synced_parts,
            })
        except MultipartServiceError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class FileListView(generics.ListAPIView):
    """Lists files accessible to the user, with pagination, filtering, and search."""
    serializer_class = StoredFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status_filter = self.request.query_params.get('status')
        search_query = self.request.query_params.get('search')
        return get_user_files(user, status=status_filter, search=search_query)

class FileDetailView(generics.RetrieveDestroyAPIView):
    """Retrieves file details or deletes file and underlying cloud object."""
    serializer_class = StoredFileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrTenantMember]
    lookup_url_kwarg = 'file_id'

    def get_object(self):
        file_obj = get_file_by_id(self.kwargs['file_id'], self.request.user)
        if not file_obj:
            raise NotFound("File not found.")
        self.check_object_permissions(self.request, file_obj)
        return file_obj

    def perform_destroy(self, instance):
        # Triggers post_delete signal in apps.files.signals which cleans up S3 object
        instance.delete()

class FileDownloadUrlView(APIView):
    """
    Generates a secure, short-lived download URL (pre-signed S3 GET or CDN).
    Supports client Range requests without streaming bytes through Django.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=DownloadUrlRequestSerializer, responses={200: OpenApiTypes.OBJECT})
    def post(self, request, file_id):
        file_obj = get_file_by_id(file_id, request.user)
        if not file_obj:
            raise NotFound("File not found.")

        serializer = DownloadUrlRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        storage = get_storage_service()
        service = DownloadService(storage)
        try:
            download_info = service.get_download_url(
                file_obj=file_obj,
                user=request.user,
                expires_in_seconds=data['expires_in'],
                as_attachment=data['as_attachment']
            )
            return Response(download_info)
        except DownloadServiceError as e:
            return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)

class FileStatusView(APIView):
    """Lightweight endpoint for polling file completion and verification status."""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses={200: StoredFileStatusSerializer})
    def get(self, request, file_id):
        file_obj = get_file_by_id(file_id, request.user)
        if not file_obj:
            raise NotFound("File not found.")
        return Response(StoredFileStatusSerializer(file_obj).data)
