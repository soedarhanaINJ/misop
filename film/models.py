from django.db import models
from datetime import date
from autoslug import AutoSlugField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
    
class MovieType(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Movie(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='media', blank=True)
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    