from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message
from .permissions import UserWriteOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response


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