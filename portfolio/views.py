from django.shortcuts import render
from . models import *


def portfolio_home(request):
    projects = Portfolio.objects.all()
    data = {
        'title' : 'Portfolio',
        'projects' : projects,
        'python' : 'img/python.svg',
        'javascript': 'img/javascript.svg',
        'nodejs': 'img/nodejs.svg',
        'html_css': 'img/code.png',
    }
    return render(request, 'portfolio/portfolio_home.html', data)

def project_detail(request, projectid):
    return render(request, 'portfolio/project_detail.html')
