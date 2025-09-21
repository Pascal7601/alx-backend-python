from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ConversationViewSet


router = DefaultRouter()

router.register("conversations", ConversationViewSet, basename="conversation")
router.register("messages", ConversationViewSet, basename="message")

urlpatterns = router.urls