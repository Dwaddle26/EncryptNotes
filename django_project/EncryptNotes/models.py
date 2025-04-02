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

# Note class, this is a Note
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} Note by {self.user.username} - Created on {self.created_at}"

# Extend user model to add a field for a user encryption key
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    encryption_key = models.TextField()
    # create and save encryption key for a user if one doesn't exist
    def save(self, *args, **kwargs):
        if not self.encryption_key:
            self.encryption_key = encrypt_user_key(generate_user_key()).decode()
        super().save(*args,**kwargs)

