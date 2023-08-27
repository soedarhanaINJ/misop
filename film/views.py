from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Movie

def index(request):
    myposting = Movie.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myposting': myposting
    }

    return HttpResponse(template.render(context, request))

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    if movie is not None:
        return render(request, 'movie.html', {'movie': movie})
    else:
        return Http404('Movie not FOunds !')