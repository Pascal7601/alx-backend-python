from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User
from django.db.models import Q


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """
    creates a new notification for every message instance
    """
    if created:
        Notification.objects.create(message=instance, user=instance.receiver)

@receiver(pre_save, sender=Message)
def log_previous_edited_msg(sender, instance, **kwargs):
    """
    logs the content of the previous message before
    it was edited to the messageHistory model
    """
    if instance.pk:
        try:
            # obtain the old message before editing
            old_instance = Message.objects.get(pk=instance.pk)
        except:
            return
        
        if old_instance.content != instance.content:
            MessageHistory.objects.create(
                message=instance,
                content=old_instance.content
            )
            # updating the is_edited to True
            instance.is_edited = True
            instance.edited_by = instance.sender

@receiver(post_delete, sender=User)
def delete_all_user_related(sender, instance, **kwargs):
    """
    deletes all notification, messages and message history when
    the user is deleted
    """ 
    Message.objects.filter(
        Q(sender=instance) | Q(receiver=instance)
    ).delete()

    Notification.objects.filter(
        user=instance
    ).delete()

    MessageHistory.objects.filter(
        Q(message__sender=instance) | Q(message__receiver=instance)
    ).delete()
