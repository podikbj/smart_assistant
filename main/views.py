from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home page',
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'About me',
    }
    return render(request, 'main/about.html', data)
