from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    num_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/info.html', {'blog': num_blog})
