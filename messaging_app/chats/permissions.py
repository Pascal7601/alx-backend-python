from rest_framework import permissions

class IsAuthenticatedUser(permissions.BasePermission):
    """checks if the user is authenticated"""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

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
        
        if request.method in ["PATCH", "PUT", "DELETE"]:
            return obj.sender == request.user
    
class IsPartOfConversation(permissions.BasePermission):
    """
    allows users who are the partcipants to view the message
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.participants.all()
        return request.user in obj.participants.all()