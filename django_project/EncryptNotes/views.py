from django.shortcuts import render
from .models import Post
from .models import Notes
from cryptography.fernet import Fernet


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'EncryptNotes/home.html', context)


def about(request):
    return render(request, 'EncryptNotes/about.html', {'title': 'About'})

def create(request):
    return render(request, 'EncryptNotes/create.html', {'title': 'Create'})
    
def announcements(request):
    return render(request, 'EncryptNotes/announcements.html', {'title': 'announcements'})

# Decrypts and lists notes for a logged in user
def list(request):
    user = request.user  
    notes = Note.objects.filter(user=user)  
    enc_user_key = user.userprofile.encryption_key
    user_key = decrypt_user_key(enc_user_key)
    decrypt_note_titles = [decrypt_data(user_key, note.title) for note in notes]
    decrypted_note_content = [decrypt_data(user_key, note.content) for note in notes]
    return render(request, 'EncryptNotes/list.html', {'title': 'Note list'})
    
# View a specific note
def view(request)
    user = request.user  
    notes = Note.objects.filter(user=user)  
    enc_user_key = user.userprofile.encryption_key
    user_key = decrypt_user_key(enc_user_key)
    return render(request, 'EncryptNotes/view.html', {'title:': {note.title}}
# Edit a specific note


