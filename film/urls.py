from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('accounts/profile/', views.profile, name='profile'),
    path('edit_profile/', views.editprofile, name='edit_profile'),
]
