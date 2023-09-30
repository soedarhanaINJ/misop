from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DeleteView
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress
from django.contrib.auth.decorators import login_required
from film.forms import UploadForm, EditProfileForm
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


class MovieDetails(generic.DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'
    

class DeleteMovieView(generic.DeleteView):
    model = Movie
    template_name = 'film/delete_movie.html'
    success_url = reverse_lazy('index')


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'editprofile/notif_edit_profile.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'facebook_url',
        'x_url',
        'instagram_url'
    ]

    success_url = reverse_lazy('index')

# User can edit their own profile
@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=UserProfile(user=request.user))
        print(request.FILES)

        if form.is_valid():
            form.save()
        
        return redirect(profile)
    
    else:
        form = EditProfileForm(instance=request.user.userprofile)

    return render(request, 'account/edit_profile.html', {'form': EditProfileForm})



def profile(request):
    email_addresses = EmailAddress.objects.filter(user=request.user)
    user_social_data = SocialAccount.objects.filter(user=request.user).first()

    if user_social_data:
        social_data = user_social_data.extra_data  # this will contain data like profile picture URL, name, etc.

    return render(request, 'account/profile.html')    
    


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
