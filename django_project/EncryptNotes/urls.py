from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='EncryptNotes-home'),
    path('about/', views.about, name='EncryptNotes-about'),
]
