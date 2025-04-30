from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .encTools import *
from tinymce.models import HTMLField

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Note class
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    # New fields for optional AI categorization
    category = models.CharField(max_length=255, blank=True, null=True)
    categorized = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} Note by {self.user.username} - Created on {self.created_at}"
