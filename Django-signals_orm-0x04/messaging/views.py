from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message
from .permissions import UserWriteOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from django.db.models import Q


@api_view(['POST'])
@permission_classes([UserWriteOrReadOnly])
def delete_user(request):
    """
    enables deletion of user's account
    """
    user = User.objects.filter(pk=request.user.id)
    if user:
        user.delete()
    
    return Response({"detail": "user succesfully deleted"})

@api_view(["GET"])
@permission_classes([UserWriteOrReadOnly])
def fetch_messages(request):
    """
    fetch all the messages and replies for specific users
    """
    msg = Message.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user), parent_message__is_null=True
        ).select_related("sender", "receiver").prefetch_related("replies__sender", "replies__receiver")

    return msg