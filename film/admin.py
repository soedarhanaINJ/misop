from django.contrib import admin
from .models import Movie, Category, UserProfile



class AdminMovie(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('id',)

admin.site.register(Movie, AdminMovie)

class AdminUserProfile(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

admin.site.register(UserProfile, AdminUserProfile)


admin.site.register(Category)
