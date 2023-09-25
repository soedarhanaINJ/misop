from django.forms import ModelForm
from django import forms
from .models import Movie, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    link = forms.TextInput()
    class Meta:
        model = Movie
        fields = ['categories', 'name', 'link', 'movietype', 'image', 'description']

class EditProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'facebook_url', 'x_url', 'instagram_url']