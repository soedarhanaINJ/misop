from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from film.forms import UploadForm, EditProfileForm, AvatarEditProfileForm
from .models import Movie, UserProfile


def index(request):
    query = Movie.objects.all()
    context = {
        'query': query
    }

    return render(request, 'index.html', context)


# MOVIE LIST
class MovieList(ListView):
    model = Movie.objects.all()
    template_name = 'film/movie.html'



# DETAILING'S MOVIE
class MovieDetailsView(DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'


# DELETE MOVIE
class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'film/delete_movie.html'
    success_url = reverse_lazy('index')


# EDIT THE AVATAR PICTURE
class EditAvatarView(UpdateView):
    model = UserProfile
    template_name = 'account/edit_avatar.html'
    form_class = AvatarEditProfileForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(EditAvatarView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        
        return context


# EDIT DATA USER PROFILE
class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = 'account/edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        
        return context


# PROFILE VIEW
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


# Function Registrations for New User
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create UserProfile after registering user
            profile = UserProfile(user=user)
            profile.save()

            # Log the user in and redirect them
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
