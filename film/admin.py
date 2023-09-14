from django.contrib import admin
from .models import Movie, Category, MovieType

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, AdminCategory)

class AdminMovie(admin.ModelAdmin):
    list_display = ('name', 'movietype')
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)

class AdminMovieType(admin.ModelAdmin):
    list_display = ('type',)

admin.site.register(MovieType, AdminMovieType)