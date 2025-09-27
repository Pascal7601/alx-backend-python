from rest_framework import permissions


class IsMessageOwnerOrReadOnly(permissions.BasePermission):
    """
    allows the one who sent the mesage to edit or delete it while others can only read
    """

    def has_object_permission(self, request, view, obj):
        # check first whether the user is part of the conversation
        if request.user not in obj.conversation.participants.all():
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.sender == request.user
    
class IsPartOfConversation(permissions.BasePermission):
    """
    allows users who are the partcipants to view the message
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.participants.all()
        return request.user in obj.participants.all()