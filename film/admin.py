from django.contrib import admin
from .models import Posting, Category

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, AdminCategory)

class AdminPosting(admin.ModelAdmin):
    list_display = ('judul_film', 'category', 'post_date')

admin.site.register(Posting, AdminPosting)