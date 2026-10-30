from typing import Optional
from django.db.models import QuerySet, Q
from apps.files.models import StoredFile, UploadSession, FileStatus

def get_user_files(
    user,
    status: Optional[str] = None,
    search: Optional[str] = None
) -> QuerySet[StoredFile]:
    """
    Selects files accessible to the user, scoped by ownership or tenant isolation.
    """
    if user.is_staff:
        qs = StoredFile.objects.all()
    else:
        user_tenant = getattr(getattr(user, 'profile', None), 'tenant_id', None)
        if user_tenant:
            qs = StoredFile.objects.filter(Q(owner=user) | Q(tenant_id=user_tenant) | Q(is_public=True))
        else:
            qs = StoredFile.objects.filter(Q(owner=user) | Q(is_public=True))

    if status:
        qs = qs.filter(status=status)

    if search:
        qs = qs.filter(original_filename__icontains=search)

    return qs.select_related('owner').order_by('-created_at')

def get_file_by_id(file_id: str, user) -> Optional[StoredFile]:
    """
    Fetches a specific file by UUID with ownership or tenant verification.
    """
    qs = get_user_files(user)
    return qs.filter(id=file_id).first()

def get_upload_session_by_id(session_id: str, user) -> Optional[UploadSession]:
    """
    Fetches an upload session ensuring owner or tenant authorization.
    """
    qs = UploadSession.objects.select_related('file', 'owner')
    if not user.is_staff:
        user_tenant = getattr(getattr(user, 'profile', None), 'tenant_id', None)
        if user_tenant:
            qs = qs.filter(Q(owner=user) | Q(tenant_id=user_tenant))
        else:
            qs = qs.filter(owner=user)
    return qs.filter(id=session_id).first()
