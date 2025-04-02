from django import forms
from tinymce.widgets import TinyMCE
from EncryptNotes.models import Note

# Form for a note
class NoteForm(forms.ModelForm):
    itle = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Note
        fields = ['title', 'content']