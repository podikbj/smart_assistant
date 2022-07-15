from django.shortcuts import render
from .models import Blog, Weather

def blog_home(request):
    blogs = Blog.objects.order_by('pub_date')
    weather = Weather.objects.all()
    data = {
        'elements' : blogs,
        'weather' : weather
    }
    return render(request, 'blog/blog_home.html', data)
