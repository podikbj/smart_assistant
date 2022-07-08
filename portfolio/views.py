from django.shortcuts import render
from . models import *


def portfolio_home(request):
    projects = Portfolio.objects.all()
    data = {
        'title' : 'Portfolio',
        'projects' : projects,
        'python' : 'main/img/python.svg',
        'javascript': 'main/img/javascript.svg',
        'nodejs': 'main/img/nodejs.svg',
        'html_css': 'main/img/code.png',

    }
    return render(request, 'portfolio/portfolio_home.html', data)

def project_detail(request):
    return render(request, 'portfolio/project_detail.html')
