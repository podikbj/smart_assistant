from django.shortcuts import render
from .models import Blog, Cities


def blog_home(request):
    blogs = Blog.objects.order_by('pub_date')
    cities = Cities.objects.all()
    data = {
        'title': 'Blog',
        'elements': blogs,
        'cities': cities
    }
    return render(request, 'blog/blog_home.html', data)


def city(request, cityid):
    cities = Cities.objects.all()
    city = Cities.objects.filter(id=cityid)
    blogs = Blog.objects.filter(city_id=cityid).order_by('pub_date')
    data = {
        'title': city[0],
        'elements': blogs,
        'cities': cities
    }
    return render(request, 'blog/blog_home.html', data)


def blog_details(request, blogid):
    blog = Blog.objects.filter(id=blogid)
    cities = Cities.objects.all()
    data = {
        'blog': blog[0],
        'cities': cities
    }
    return render(request, 'blog/blog_details.html', data)
