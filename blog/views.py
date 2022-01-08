import datetime
from django.shortcuts import render

from .models import Post
from .forms import AddPostForm



def index(request):
    posts = Post.objects
    context = {
        'post': posts,
    }

    return render(request, 'index.html', context)


def add_post(request):
    # Your code here
    pass
