from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
# Form for a note
class NoteForm(forms.ModelForm):
    itle = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Note
        fields = ['title', 'content']