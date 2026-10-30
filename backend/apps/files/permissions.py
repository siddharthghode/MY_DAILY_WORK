from rest_framework import permissions

class IsOwnerOrTenantMember(permissions.BasePermission):
    """
    Object-level permission allowing access only to the file/session owner,
    members of the same tenant, or staff/administrators.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Public files can be read by any authenticated user
        if getattr(obj, 'is_public', False) and request.method in permissions.SAFE_METHODS:
            return True

        # Staff can access everything
        if request.user.is_staff:
            return True

        # Check ownership
        owner = getattr(obj, 'owner', None)
        if owner == request.user:
            return True

        # Check tenant isolation
        user_tenant = getattr(getattr(request.user, 'profile', None), 'tenant_id', None)
        obj_tenant = getattr(obj, 'tenant_id', None)
        if user_tenant and obj_tenant and user_tenant == obj_tenant:
            return True

        return False
