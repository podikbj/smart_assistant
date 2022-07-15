from django.shortcuts import render
from .models import MyApps

def index(request):
    my_apps = MyApps.objects.order_by('id')
    data = {
        'title': 'Smart assistant',
        'elements': my_apps,

    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'ABOUT',
    }
    return render(request, 'main/about.html', data)
