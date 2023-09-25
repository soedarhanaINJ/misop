from django.contrib import admin
from .models import Movie, Category



class AdminMovie(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)

admin.site.register(Category)
