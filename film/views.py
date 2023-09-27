from typing import Any
from django.db import models
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from film.forms import UploadForm, EditProfileForm
from .models import Movie, UserProfile


def index(request):
    query = Movie.objects.all()
    context = {
        'query': query
    }

    return render(request, 'index.html', context)

def movie(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)

    return render(request, 'film/movie.html', {'movies': movies})
    

def profile(request):
    email_addresses = EmailAddress.objects.filter(user=request.user)
    user_social_data = SocialAccount.objects.filter(user=request.user).first()

    if user_social_data:
        social_data = user_social_data.extra_data  # this will contain data like profile picture URL, name, etc.

    return render(request, 'account/profile.html')    
    

# Functions upload for user can upload with herself
@login_required    
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()

        return redirect(index)

    return render(request, 'film/upload.html', {'form': UploadForm})


# User can edit their own profile
@login_required
def editprofile(request):
    if request.method == 'POST':
        editprofile_form = EditProfileForm(request.POST, request.FILES)
        

        if editprofile_form.is_valid():
            editprofile_form.save()
        
    else:
        editprofile_form = EditProfileForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'editprofile_form': editprofile_form})



class MovieDetails(generic.DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'