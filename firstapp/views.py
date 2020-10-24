from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'news/index.html',
        {
            "posts": posts
        }
    )