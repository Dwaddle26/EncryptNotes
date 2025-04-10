from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='EncryptNotes-home'),
    path('about/', views.about, name='EncryptNotes-about'),
    path('create/', views.create, name='EncryptNotes-create'),
    path('announcements/', views.announcements, name='EncryptNotes-announcements'),
    path('list/', views.create, name='EncryptNotes-list'),
    path('edit/', views.create, name='EncryptNotes-edit'),
    path('view/', views.create, name='EncryptNotes-view')
    
    
    
]
