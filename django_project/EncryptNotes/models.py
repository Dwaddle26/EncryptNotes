from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def Note(request):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete)

