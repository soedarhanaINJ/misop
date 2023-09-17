from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.template import loader
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress

from film.forms import UploadForm
from .models import Movie


def index(request):
    query = Movie.objects.all()

    return render(request, 'index.html', {'query': query})

def movie(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)

    if movie is not None:
        return render(request, 'film/movie.html', {'movies': movies})
    else:
        return Http404('Movie not FOunds !')
    
    

# Functions upload for user can upload with herself    
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()

        return redirect(index)

    return render(request, 'film/upload.html', {'form': UploadForm})


def profile(request):
    email_addresses = EmailAddress.objects.filter(user=request.user)
    user_social_data = SocialAccount.objects.filter(user=request.user).first()

    if user_social_data:
        social_data = user_social_data.extra_data  # this will contain data like profile picture URL, name, etc.

    return render(request, 'account/profile.html')