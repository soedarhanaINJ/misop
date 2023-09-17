from . import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('accounts/profile/', views.profile, name='profile'),
]
