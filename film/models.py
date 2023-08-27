from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=155)
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    