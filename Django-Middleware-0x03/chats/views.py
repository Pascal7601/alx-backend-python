from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Conversation, Message
from .serializers import MessageSerializer, CoversationSerializer
from .permissions import IsAuthenticatedUser, IsMessageOwnerOrReadOnly, IsPartOfConversation
from rest_framework.response import Response
from .pagination import MessagePagination
from .filters import MessageFilter
from django_filters.rest_framework import DjangoFilterBackend


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticatedUser, IsMessageOwnerOrReadOnly, IsPartOfConversation]
    pagination_class = MessagePagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = [MessageFilter]


    def get_queryset(self):
        # only return conversations that the user is part of
        return Message.objects.filter(conversation__participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """Send a new message to an existing conversation"""
        conversation_id = request.data.get("conversation")
        if not conversation_id:
            return Response({"detail: conversation_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            conversation = Conversation.objects.get(pk=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"detail: conversation not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user not in conversation.participants.all():
            return Response({"detail: not a participant of this convo"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user, conversation=conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = CoversationSerializer
    queryset = Conversation.objects.all()
    permission_classes = [IsAuthenticatedUser, IsPartOfConversation]

    def get_queryset(self):
        # return only the convo that the user is part of
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """Create a new conversation with participants"""
        participants_ids = request.data.get("participants", [])
        if not participants_ids:
            return Response({"detail": "At least one participant is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        participants_ids = [int(pid) for pid in participants_ids]

        if request.user.user_id not in participants_ids:
            participants_ids.append(request.user.user_id)

        conversation = Conversation.objects.create()
        conversation.participants.set(participants_ids)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)