from . import views
from django.urls import path
from film.views import MovieDetails, MovieList


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', MovieList.as_view(), name='movie'),
    path('accounts/profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='edit_profile'),
    path('details/<int:pk>', MovieDetails.as_view(), name='moviedetails'),
]
