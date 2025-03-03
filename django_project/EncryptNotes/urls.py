from django.urls import path
from .import views

urlpatterns = [
    # Define a URL pattern for the home page.
    # '' (empty string) represents the root URL.
    # views.home is the view function that will handle requests to this URL.
    # name='EncryptNotes-home' assigns a name to this URL pattern, which can be used for reverse URL lookup.
    path('', views.home, name='EncryptNotes-home'),

    # Define a URL pattern for the about page.
    # 'about/' represents the URL path for the about page.
    # views.about is the view function that will handle requests to this URL.
    # name='EncryptNotes-about' assigns a name to this URL pattern.
    path('about/', views.about, name='EncryptNotes-about'),
]