from django.contrib import admin
from . import models


# Register Custom User
@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_full_name', 'is_active', ]


# Register Catagory model
@admin.register(models.Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('translation', )}


# Register Tag model
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'translation', 'slug', ]
    list_display_links = ['title', ]
    prepopulated_fields = {'slug': ('translation', )}


# Register Post model
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'catagory',
        'published_at', 'status', 'featured',
    ]
    list_filter = ['author', 'catagory', 'status', 'featured', ]
    prepopulated_fields = {'slug': ('translation', )}

