from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.template import loader

from film.forms import UploadForm
from .models import Movie

def index(request):
    return render(request, 'index.html')

def movie(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)

    if movie is not None:
        return render(request, 'movie.html', {'movies': movies})
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

    return render(request, 'upload.html', {'form': UploadForm})