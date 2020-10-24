from django.contrib import admin
from .models import Post


# class PostAdmin(admin.ModelAdmin):
#     Model = Post
#     list_display = ('title', 'created', 'author')

admin.site.register(Post)