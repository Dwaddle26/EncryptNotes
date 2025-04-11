from django.shortcuts import render, redirect
from .models import Post
from .models import Note
from cryptography.fernet import Fernet
from .encTools import *
from .forms import NoteForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'EncryptNotes/home.html', context)


def about(request):
    return render(request, 'EncryptNotes/about.html', {'title': 'About'})
    
def announcements(request):
    return render(request, 'EncryptNotes/announcements.html', {'title': 'announcements'})

# Creates a note, encrypts it, saves to database
def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            ukey = decrypt_user_key(request.user.userprofile.encryption_key)
            print(f"Decryption Key: {ukey}")
            nTitle = form.cleaned_data['title']
            nContent = form.cleaned_data['content']
            encTitle = encrypt_data(ukey, nTitle).decode()
            encContent = encrypt_data(ukey, nContent).decode()
            
            Note.objects.create(
            user = request.user,
            title = encTitle,
            content = encContent
            )
            return redirect('EncryptNotes-list')
    else:
        #GET request needs an empty note form
        form = NoteForm()
        
    return render(request, 'EncryptNotes/create.html', {'form': form, 'title': 'Create'})

# Decrypts and lists notes for a logged in user
def list(request):
    user = request.user
    ukey = decrypt_user_key(request.user.userprofile.encryption_key)
    print(f"Decryption Key: {ukey}")
    notes = Note.objects.filter(user=user)
    #noteTitles = [decrypt_data(ukey, note.title) for note in notes]
    #noteContents = [decrypt_data(ukey, note.content) for note in notes]
    #noteID = [decrypt_data(ukey, note.id) for note in notes]
    noteList = [
        {'id': note.id, 'title': decrypt_data(ukey, note.title.encode()), 'content': decrypt_data(ukey, note.content.encode()) 
        }
        for note in notes
    ]
    #print(f"Encrypted Title: {note.title}, Encrypted Content: {note.content}")
    return render(request, 'EncryptNotes/list.html', {'notes': noteList})

# View a specific note
def view(request, note_id):
    user = request.user  
    note = Note.objects.get(id=note_id, user=user)  
    eukey = user.userprofile.encryption_key
    ukey = decrypt_user_key(eukey)
    thisTitle = decrypt_data(ukey, note.title.encode())
    thisNote = decrypt_data(ukey, note.content.encode())
    #FIX THIS
    return render(request, 'EncryptNotes/view.html', {'title': thisTitle, 'note': thisNote})


# Edit a specific note
def edit(request, note_id):
    user = request.user
    note = Note.objects.get(id=note_id, user=user)
    ukey = decrypt_user_key(user.userprofile.encryption_key)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            editedTitle = form.cleaned_data['title']
            editedContent = form.cleaned_data['content']
            encTitle = encrypt_data(ukey, editedTitle).decode()
            encContent = encrypt_data(ukey, editedNote).decode()
            note.title = encTitle
            note.content = encContent
            note.save()
            return redirect('EncryptNotes/list.html')
    else:
        clearTitle = decrypt_data(ukey, note.title.encode())
        clearContent = decrypt_data(ukey, note.content.encode())
        form = NoteForm(initial={'title': clearTitle, 'content': clearContent})
    
    return render(request, 'EncryptNotes/edit.html', {'form': form, 'title': 'Edit Note'})