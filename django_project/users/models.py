from django.db import models
from django.contrib.auth.models import User
from EncryptNotes.encTools import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
        
# Extend user model to add a field for a user encryption key
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    encryption_key = models.TextField()
    # create and save encryption key for a user if one doesn't exist
    def save(self, *args, **kwargs):
        if not self.encryption_key:
            self.encryption_key = encrypt_user_key(generate_user_key()).decode()
        super().save(*args,**kwargs)
