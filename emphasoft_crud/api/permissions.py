from rest_framework import permissions


class CreateOrSelfOrAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to create new user or allow user or admin only
    to update user info.
    """

    # def has_permission(self, request, view):
    #     if (request.method == 'POST' or
    #             request.method in permissions.SAFE_METHODS or
    #             (request.user and request.user.is_staff)):
    #         return True

    def has_object_permission(self, request, view, obj):
        return (
                request.method in permissions.SAFE_METHODS or
                obj == request.user or
                (request.user and request.user.is_staff))
