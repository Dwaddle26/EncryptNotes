from django import forms
from tinymce.widgets import TinyMCE
from EncryptNotes.models import Note

# Form for a note
class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    categorized = forms.BooleanField(required=False, initial=False)
    category = forms.CharField(required=False, max_length=255)
    class Meta:
        model = Note
        fields = ['title', 'content', 'categorized', 'category']