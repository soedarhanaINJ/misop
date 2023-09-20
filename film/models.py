from django.db import models
from datetime import date
from allauth.account.forms import UserForm
from django.contrib.auth.models import User

CHOICE_MOVIETYPE = (
    (0, 'Kids'),
    (1, 'teenager'),
    (2, 'mature'),
)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class MovieType(models.Model):
    type = models.IntegerField(choices=CHOICE_MOVIETYPE, default=1)

class Movie(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='media', blank=True)
    movietype = models.ForeignKey(MovieType, on_delete=models.CASCADE, default=1)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    x_url = models.CharField(max_length=255, blank=True)
    instagram_url = models.CharField(max_length=255, blank=True)