from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj == request.user


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or bool(
            request.user and request.user.is_superuser)
