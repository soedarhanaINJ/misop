from django.forms import ModelForm
from django import forms
from .models import Movie, UserProfile

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    link = forms.TextInput()
    class Meta:
        model = Movie
        fields = ['categories', 'name', 'link', 'movietype', 'image', 'description']



class EditProfileForm(ModelForm):
    avatar = forms.ImageField()
    username = forms.CharField()
    email = forms.CharField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    facebook_url = forms.CharField(max_length=255)
    x_url = forms.CharField(max_length=255)
    instagram_url = forms.CharField(max_length=255)
    

    class Meta:
        model = UserProfile
        fields = ['avatar', 'username', 'first_name', 'last_name', 'email', 'facebook_url', 'x_url', 'instagram_url']