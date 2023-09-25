from django.forms import ModelForm
from django import forms
from .models import Movie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    link = forms.TextInput()
    class Meta:
        model = Movie
        fields = ['categories', 'name', 'link', 'movietype', 'image', 'description']
