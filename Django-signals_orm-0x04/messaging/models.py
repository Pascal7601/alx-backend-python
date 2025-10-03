from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE, related_name="edited_messages")
    edited_at = models.DateTimeField(auto_now=True)
    parent_message = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    def __str__(self):
        if self.parent_message:
            return f"{self.sender.username} sent a reply to {self.receiver.username}"
        return f"message from {self.sender.username} to {self.receiver.username}"
    
class Notification(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("message", "user")
    
    def __str__(self):
        return f"notification for {self.user.username} about message: {self.message.id}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)