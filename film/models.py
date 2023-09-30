from django.db import models
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
    

class Movie(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(unique=True, max_length=255, blank=True)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='tumbnails', blank=True)
    movietype = models.IntegerField(choices=CHOICE_MOVIETYPE)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=False, blank=True)
    avatar = models.ImageField(default='avatar/avatar.jpg', upload_to='avatar', blank=True)
    email = models.CharField(unique=True, max_length=55, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    x_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)
