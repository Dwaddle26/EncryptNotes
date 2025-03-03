from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Path for the Django admin interface.
    # 'admin/' is the URL path for the admin site.
    # admin.site.urls includes all the URLs defined for the admin interface.
    path('admin/', admin.site.urls),

    # Include the URL patterns from the 'EncryptNotes' app.
    # '' (empty string) represents the root URL.
    # include('EncryptNotes.urls') includes all the URLs defined in the 'urls.py' file of the 'EncryptNotes' app.
    # This allows you to modularize your URLs by defining them in separate app-level 'urls.py' files.
    path('', include('EncryptNotes.urls')),
]