from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import MessageSerializer, CoversationSerializer
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Send a new message to an existing conversation"""
        data = request.data.copy()
        data["sender"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = CoversationSerializer
    queryset = Conversation.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new conversation with participants"""
        participants_ids = request.data.get("participants", [])
        conversation = Conversation.objects.create()
        conversation.participants.set(participants_ids)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)