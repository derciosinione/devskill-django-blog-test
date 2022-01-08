import datetime
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Post
from .forms import AddPostForm



def index(request):
    posts = Post.objects.order_by('-date')
    context = {
        'posts': posts,
    }
    
    return render(request, 'blog.html', context)




def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES,)
        
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            messages.error(
                request, f'{form.errors}')
    else:
        form = AddPostForm()
        
    return render(request, 'add_post.html', {'form': form})