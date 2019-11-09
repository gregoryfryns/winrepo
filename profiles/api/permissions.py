from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


# class IsSelfOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view, obj):
#         if request.method == permissions.SAFE_METHODS:
#             return True

#         return obj.user is not None and obj.user == request.user
