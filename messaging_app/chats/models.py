from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4, db_index=True)
    email = models.EmailField(unique=True)
    phone_number = models.TextField(null=True)
    password_hash = models.TextField(null=False) # to be modified

    class Role(models.TextChoices):
        GUEST = "Guest", "guest"
        HOST = "Host", "host"
        ADMIN = "Admin", "admin"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.GUEST)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password_hash"]

    def __str__(self):
        return f"{self.email} ({self.role})"


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    partcipants = models.ManyToManyField(User, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"conversation {self.conversation_id}"


class Message(models.Model):
    """message model"""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message from {self.sender.email}: {self.message_body} at {self.sent_at}"
