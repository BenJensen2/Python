from django.db import models
from login.models import UserManager, User

class Message(models.Model):
    message = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# A user can like many posts and a post can have many likes: Many to Many
    user = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message,related_name="message_comments", on_delete=models.CASCADE)