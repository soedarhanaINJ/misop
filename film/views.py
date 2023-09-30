from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from film.forms import UploadForm, EditProfileForm, AvatarEditProfileForm
from .models import Movie, UserProfile


def index(request):
    query = Movie.objects.all()
    context = {
        'query': query
    }

    return render(request, 'index.html', context)

class MovieList(ListView):
    model = Movie.objects.all()
    template_name = 'film/movie.html'


class MovieDetailsView(DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'
    

class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'film/delete_movie.html'
    success_url = reverse_lazy('index')


class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = 'account/edit_profile.html'
    fields = [
        'avatar',
        'username',
        'first_name',
        'last_name',
        'email',
        'facebook_url',
        'x_url',
        'instagram_url'
    ]
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        
        return context


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'account/profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        
        return context
    


# Functions upload for user can upload movie with herself   
@login_required    
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        #print(request.FILES)

        if form.is_valid():
            form.save()

        return redirect(index)

    return render(request, 'film/upload.html', {'form': UploadForm})
