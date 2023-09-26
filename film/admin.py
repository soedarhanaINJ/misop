from django.contrib import admin
from .models import Movie, Category, UserProfile



class AdminMovie(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)
admin.site.register(UserProfile)
admin.site.register(Category)
