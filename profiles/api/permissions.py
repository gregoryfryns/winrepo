from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsSelf(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        return obj.user is not None and obj.user == request.user
