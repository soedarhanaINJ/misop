from django.contrib import admin
from .models import Movie, Category, MovieType



class AdminMovie(admin.ModelAdmin):
    list_display = ('name', 'movietype')
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)

admin.site.register(Category)
admin.site.register(MovieType)
