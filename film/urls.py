from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/upload', views.upload, name='upload'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('movielist/', views.movielist, name='movielist'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)