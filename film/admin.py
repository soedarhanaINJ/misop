from django.contrib import admin
from .models import Movie, Category

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, AdminCategory)

class AdminMovie(admin.ModelAdmin):
    list_display = ('name', 'category', 'post_date')
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)