from . import views
from django.urls import path
from film.views import MovieDetails


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('accounts/profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='edit_profile'),
    path('details/<int:pk>', MovieDetails.as_view(), name='moviedetails'),
]
