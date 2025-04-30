from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Note
from cryptography.fernet import Fernet
from .encTools import *
from .forms import NoteForm
from django.utils.html import strip_tags
from .aiTools import *

def home(request):
    if request.user.is_authenticated:
        # Redirect to the List Notes page if the user is authenticated
        return redirect('EncryptNotes-list')
    else:
        # Redirect to the Login page if the user is not authenticated
        return redirect('login')

@login_required
def list(request):
    user = request.user
    ukey = decrypt_user_key(request.user.userprofile.encryption_key)
    #print(f"Decryption Key: {ukey}")  # Debugging output

    notes = Note.objects.filter(user=user)
    noteList = []
    for note in notes:
        try:
            # Decrypt the title and content
            decrypted_title = decrypt_data(ukey, note.title.encode())
            decrypted_content = decrypt_data(ukey, note.content.encode())
            #print(f"Decrypted Title: {decrypted_title}, Decrypted Content: {decrypted_content}")  # Debugging output

            # Sanitize the content to remove unwanted tags
            sanitized_content = strip_tags(decrypted_content)
            
            if note.categorized:
                category = note.category 
            else:
                category = None

            noteList.append({
            'id': note.id, 
            'title': decrypted_title, 
            'content': sanitized_content,
            'category': category
            })
        except Exception as e:
            print(f"Error decrypting note {note.id}: {e}")
            continue

    #print(f"Decrypted Notes: {noteList}")
    return render(request, 'EncryptNotes/list.html', {'notes': noteList})


def about(request):
    return render(request, 'EncryptNotes/about.html', {'title': 'About'})
    
def announcements(request):
    return render(request, 'EncryptNotes/announcements.html', {'title': 'announcements'})

# Creates a note, encrypts it, saves to database
def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Retrieve the user's decryption key
            ukey = decrypt_user_key(request.user.userprofile.encryption_key)
            #print(f"Decryption Key: {ukey}")  # Debugging output

            # Get the title and content from the form
            nTitle = form.cleaned_data['title']
            nContent = form.cleaned_data['content']
            #print(f"Original Title: {nTitle}, Original Content: {nContent}")  # Debugging output

            # Encrypt the title and content
            encTitle = encrypt_data(ukey, nTitle).decode()
            encContent = encrypt_data(ukey, nContent).decode()
            #print(f"Encrypted Title: {encTitle}, Encrypted Content: {encContent}")  # Debugging output
            
            categorized = form.cleaned_data.get('categorized')
            category = None 
            if categorized:
                category = categorize_note(nContent)
                
            Note.objects.create(
                user=request.user,
                title=encTitle,
                content=encContent,
                category=category,
                categorized=categorized
            )
            return redirect('EncryptNotes-home')
    else:
        form = NoteForm()
    return render(request, 'EncryptNotes/create.html', {'form': form, 'title': 'Create'})

# Decrypt and view a specific note
def view(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    ukey = decrypt_user_key(request.user.userprofile.encryption_key)

    # Decrypt the title and content
    decrypted_title = decrypt_data(ukey, note.title.encode())
    decrypted_content = decrypt_data(ukey, note.content.encode())
    #print(f"Decrypted Title: {decrypted_title}, Decrypted Content: {decrypted_content}")  # Debugging output

    # Sanitize the content to remove unwanted tags
    sanitized_content = strip_tags(decrypted_content)

    return render(request, 'EncryptNotes/view.html', {
        'title': decrypted_title,
        'content': sanitized_content,
        'note': note
    })


# Edit a specific note
def edit(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    ukey = decrypt_user_key(request.user.userprofile.encryption_key)
    categorization = form.cleaned_data.get('categorized')
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # Encrypt the updated title and content
            updated_title = encrypt_data(ukey, form.cleaned_data['title']).decode()
            updated_content = encrypt_data(ukey, form.cleaned_data['content']).decode()
            
            note.title = updated_title
            note.content = updated_content
            note.categorized = categorization
            if categorization:
                note.category = categorize_note(form.cleaned_data['content'].decode())
            else:
                note.category = None
                
            note.save()
            return redirect('EncryptNotes-home')
    else:
        # Decrypt the title and content for editing
        decrypted_title = decrypt_data(ukey, note.title.encode())
        decrypted_content = decrypt_data(ukey, note.content.encode())
        
        sanitized_content = strip_tags(decrypted_content)

        # Pre-fill the form with decrypted and sanitized data
        form = NoteForm(initial={
        'title': decrypted_title,
        'content': sanitized_content,
        'categorized': note.categorized
    })

    return render(request, 'EncryptNotes/edit.html', {'form': form, 'note': note})

# Delete a specific note
def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    ukey = decrypt_user_key(request.user.userprofile.encryption_key)
    #print(f"Decryption Key: {ukey}")  # Debugging output

    # Decrypt the note title for display
    try:
        decrypted_title = decrypt_data(ukey, note.title.encode())
        #print(f"Decrypted Title: {decrypted_title}")  # Debugging output
    except Exception as e:
        print(f"Error decrypting title for note {note.id}: {e}")
        decrypted_title = "Error decrypting title"

    if request.method == 'POST':
        note.delete()
        return redirect('EncryptNotes-home')

    return render(request, 'EncryptNotes/delete.html', {'note': note, 'decrypted_title': decrypted_title})