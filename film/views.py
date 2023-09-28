from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import ListView
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
    model = Movie
    template_name = 'film/movie.html'


class MovieDetails(generic.DetailView):
    model = Movie
    template_name = 'film/moviedetail.html'
    

def profile(request):
    email_addresses = EmailAddress.objects.filter(user=request.user)
    user_social_data = SocialAccount.objects.filter(user=request.user).first()

    if user_social_data:
        social_data = user_social_data.extra_data  # this will contain data like profile picture URL, name, etc.

    return render(request, 'account/profile.html')    
    


# User can edit their own profile
@login_required
def editprofile(request):
    if request.POST:
        editprofile_form = EditProfileForm(request.POST, request.FILES, instance=UserProfile(user=request.user))
        print(request.FILES)

        if editprofile_form.is_valid():
            editprofile_form.save()
        
        return redirect(profile)

    return render(request, 'account/edit_profile.html', {'editprofile_form': EditProfileForm})





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
