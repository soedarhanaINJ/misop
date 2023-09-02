from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from user.forms import LoginForm


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm

