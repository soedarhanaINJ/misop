from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('movies/details/<int:movie_id>', views.moviedetail, name='moviedetail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('edit_profile/', views.editprofile, name='edit_profile'),
]
