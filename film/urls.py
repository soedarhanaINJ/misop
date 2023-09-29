from . import views
from django.urls import path
from film.views import MovieDetails, MovieList, EditProfilePageView


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:id>', MovieList.as_view(), name='movie'),
    path('accounts/profile/', views.profile, name='profile'),
    path('<int:pk>/editprofilepage/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('details/<int:pk>', MovieDetails.as_view(), name='moviedetails'),
]
