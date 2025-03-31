from django.shortcuts import render
from .models import Post
from .models import Note
from cryptography.fernet import Fernet
from .encTools import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'EncryptNotes/home.html', context)


def about(request):
    return render(request, 'EncryptNotes/about.html', {'title': 'About'})
    
def announcements(request):
    return render(request, 'EncryptNotes/announcements.html', {'title': 'announcements'})
    
def create(request):
    if request.method == 'POST
    return render(request, 'EncryptNotes/create.html', {'title': 'Create'})

# Decrypts and lists notes for a logged in user
def list(request):
    user = request.user  
    notes = Note.objects.filter(user=user)  
    eukey = user.userprofile.encryption_key
    ukey = decrypt_user_key(eukey)
    noteTitles = [decrypt_data(ukey, note.title) for note in notes]
    noteContents = [decrypt_data(ukey, note.content) for note in notes]
    return render(request, 'notes/list.html', {'notes': noteContents})

# View a specific note
def view(request, note_id):
    user = request.user  
    note = Note.objects.get(id=note_id, user=user)  
    eukey = user.userprofile.encryption_key
    ukey = decrypt_user_key(eukey)
    thisTitle = decrypt_data(ukey, note.title)
    thisNote = decrypt_data(ukey, note.content)
    #FIX THIS
    return render(request, 'EncryptNotes/view.html', {'title:': {note.title} 'note': thisNote})

# Edit a specific note
def edit(request, note_id):
    user = request.user
    note = Note.objects.get(id=note_id, user=user)
    if request.method == 'POST':
        ukey = decrypt_user_key(user.userprofile.encryption_key)
        editedNote = request.POST['content']
        enc_content = encrypt_data(user_key, editedNote)
        note.content = enc_content
        note.save()
        return HttpResponseRedirect('/EncryptNotes/list')
    
    ukey = decrypt_user_key(user.userprofile.encryption_key)
    thisNote = decrypt_data(ukey, note.note_content)
    thisTitle = 
    return render(request, 'notes/edit.html', {'note': thisNote})



