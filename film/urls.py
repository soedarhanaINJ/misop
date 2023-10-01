from . import views
from django.urls import path
from film.views import MovieDetailsView, MovieList, EditAvatarView, DeleteMovieView, UserProfileView, EditProfilePageView


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:id>', MovieList.as_view(), name='movie'),
    path('details/<int:pk>', MovieDetailsView.as_view(), name='moviedetails'),
    path('<int:pk>/change-avatar/', EditAvatarView.as_view(), name='edit_avatar'),
    path('movies/<int:pk>/delete', DeleteMovieView.as_view(), name='delete_movie'),
    path('accounts/profile/<int:pk>/', UserProfileView.as_view(), name='profile_view'),    
    path('<int:pk>/edit-profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
