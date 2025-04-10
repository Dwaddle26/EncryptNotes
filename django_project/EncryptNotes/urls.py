from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='EncryptNotes-home'),
    path('about/', views.about, name='EncryptNotes-about'),
    path('create/', views.create, name='EncryptNotes-create'),
    path('announcements/', views.announcements, name='EncryptNotes-announcements'),
    path('list/', views.list, name='EncryptNotes-list'),
    path('edit/<int:note_id>', views.edit, name='EncryptNotes-edit'),
    path('view/<int:note_id>/', views.view, name='EncryptNotes-view')
    
    
    
]
