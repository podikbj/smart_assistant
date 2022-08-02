from django.shortcuts import render
from .models import Blog, Cities
import requests
from django.core.paginator import Paginator
from django.shortcuts import render

cities = Cities.objects.all()

def getWeatherForCities(city=None):
    appid = '56ffc629eee1d5c798c571d37f907536'
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid=' + appid
    all_cities = []
    if city != None:
        res = requests.get(url.format(city.lat, city.lon)).json()
        weather_info = {
            'city': city.city_name,
            'temp': round(res["main"]["temp"]),
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(weather_info)
        return all_cities

    for city in cities:
        res = requests.get(url.format(city.lat, city.lon)).json()
        weather_info = {
            'city': city.city_name,
            'temp': round(res["main"]["temp"]),
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(weather_info)
    return all_cities

def blog_home(request):
    blog_list = Blog.objects.order_by('pub_date')
    paginator = Paginator(blog_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_cities = getWeatherForCities()

    data = {
        'title': 'Welcome to my travel blog!',
        'elements': page_obj,
        'cities': cities,
        'blogs': blog_list,
        'all_cities' : all_cities
    }
    return render(request, 'blog/blog_home.html', data)


def city(request, city_id):
    city = Cities.objects.get(id=city_id)
    all_cities = getWeatherForCities(city)
    blogs = Blog.objects.filter(city_id=city_id).order_by('pub_date')

    data = {
        'title': city.city_name,
        'elements': blogs,
        'cities': cities,
        'all_cities': all_cities
    }
    return render(request, 'blog/blog_home.html', data)


def blog_details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    city = Cities.objects.get(id=blog.city_id)
    all_cities = getWeatherForCities(city)
    data = {
        'blog': blog,
        'cities': cities,
        'all_cities': all_cities
    }
    return render(request, 'blog/blog_details.html', data)
