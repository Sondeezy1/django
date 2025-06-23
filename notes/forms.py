from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'categorie', 'termine']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu', 'rows': 4}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'termine': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]