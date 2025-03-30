from django.contrib import admin
from .models import Post
from .models import Note

admin.site.register(Post)
admin.site.register(Note)