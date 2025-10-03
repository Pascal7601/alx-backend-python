from rest_framework.permissions import BasePermission


class UserWriteOrReadOnly(BasePermission):
    """only users who send the message are able to delete or edit it"""

    def has_object_permission(self, request, view, obj):
        return self.request.user == obj.sender