from django.shortcuts import redirect, render
from django.http import Http404
from django.views import generic
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress

from film.forms import UploadForm
from .models import Movie


def index(request):
    query = Movie.objects.all()
    context = {
        'query': query
    }

    return render(request, 'index.html', context)

def movie(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)

    return render(request, 'film/movie.html', {'movies': movies})
    
    
    

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


def editprofile(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name

    return render(request, 'account/edit_profile.html')

class MovieDetails(generic.DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'