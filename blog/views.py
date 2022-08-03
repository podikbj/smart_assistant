from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Blog, Cities
import requests
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

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

class BlogHome(ListView):
    model = Blog
    template_name = 'blog/blog_home.html'
    context_object_name = 'blogs'
    paginate_by = 4  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to my travel blog!'
        context['all_cities'] = getWeatherForCities()
        return context

    def get_queryset(self):
            return Blog.objects.order_by('pub_date')

# def blog_home(request):
#     blog_list = Blog.objects.order_by('pub_date')
#     paginator = Paginator(blog_list, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     all_cities = getWeatherForCities()
#
#     data = {
#         'title': 'Welcome to my travel blog!',
#         'elements': page_obj,
#         'cities': cities,
#         'blogs': blog_list,
#         'all_cities' : all_cities
#     }
#     return render(request, 'blog/blog_home.html', data)

class CityListView(ListView):
    model = Blog
    template_name = 'blog/blog_home.html'
    allow_empty = False
    paginate_by = 19  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to my travel blog!'
        context['all_cities'] = getWeatherForCities()
        return context

    def get_queryset(self):
        return Blog.objects.filter(city_id=self.kwargs['city_id'])

# def city(request, city_id):
#     city = get_object_or_404(Cities, id=city_id)
#     all_cities = getWeatherForCities(city)
#     blogs = Blog.objects.filter(city_id=city_id).order_by('pub_date')
#
#     data = {
#         'title': city.city_name,
#         'elements': blogs,
#         'cities': cities,
#         'all_cities': all_cities
#     }
#     return render(request, 'blog/blog_home.html', data)


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    city = get_object_or_404(Cities, id=blog.city_id)
    all_cities = getWeatherForCities(city)
    data = {
        'blog': blog,
        'cities': cities,
        'all_cities': all_cities
    }
    return render(request, 'blog/blog_details.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
