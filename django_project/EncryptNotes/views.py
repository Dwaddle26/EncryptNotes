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
    return render(request, 'EncryptNotes/create.html', {'title': 'create'})
    
def announcements(request):
    return render(request, 'EncryptNotes/announcements.html', {'title': 'announcements'})

# Decrypts and lists notes for a user
def list_user_notes(request):
    user = request.user  
    notes = Note.objects.filter(user=user)  
    enc_user_key = user.userprofile.encryption_key
    user_key = decrypt_user_key(enc_user_key)
    decrypt_note_titles = [decrypt_data(user_key, note.title) for note in notes]
    decrypted_note_content = [decrypt_data(user_key, note.content) for note in notes]
    return render(request, 'notes/listNotes.html', {'title': 'Note list'})


