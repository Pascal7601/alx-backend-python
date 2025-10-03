from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, Notification


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """
    creates a new notification for every message instance
    """
    if created:
        Notification.objects.create(message=instance, user=instance.receiver)

