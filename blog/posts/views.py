from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    template = 'posts/index.html'
    return render(request, template, context)
