from django.contrib import admin
from .models import Post, Comment
@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created', 'updated', 'published', 'body']

@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created', 'active', 'comment']