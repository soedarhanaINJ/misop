from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))