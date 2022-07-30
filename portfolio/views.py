from django.shortcuts import render
from . models import *


def portfolio_home(request):
    projects = Portfolio.objects.all()
    data = {
        'title' : 'Portfolio',
        'projects' : projects,
        'python' : 'img/python.png',
        'javascript': 'img/java-script.png',
        'nodejs': 'img/nodejs.png',
        'html_css': 'img/browser.png',
    }
    return render(request, 'portfolio/portfolio_home.html', data)

def project_detail(request, projectid):
    return render(request, 'portfolio/project_detail.html')
