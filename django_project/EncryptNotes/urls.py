from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='EncryptNotes-home'),
    path('list/', views.list, name='EncryptNotes-list'),
    path('about/', views.about, name='EncryptNotes-about'),
    path('create/', views.create, name='EncryptNotes-create'),
    path('category/<path:category>/', views.category_list, name='EncryptNotes-category'),
    path('announcements/', views.announcements, name='EncryptNotes-announcements'),
    path('edit/<int:note_id>', views.edit, name='EncryptNotes-edit'),
    path('view/<int:note_id>/', views.view, name='EncryptNotes-view'),
    path('delete/<int:note_id>/', views.delete, name='EncryptNotes-delete'),
    path('tinymce/', include('tinymce.urls')),
]
