from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ConversationViewSet
from django.urls import path, include


router = DefaultRouter()

router.register("conversations", ConversationViewSet, basename="conversation")
router.register("messages", MessageViewSet, basename="message")


urlpatterns = [
    path('', include(router.urls)),
]