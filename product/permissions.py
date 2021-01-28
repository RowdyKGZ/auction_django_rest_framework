from rest_framework import permissions


class IsOwnerUser(permissions.BasePermission):
    """permission for check user is author"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or bool(
            request.user and request.user.is_superuser)
