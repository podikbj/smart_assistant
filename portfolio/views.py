from django.shortcuts import render
from .models import *


def portfolio_home(request):
    projects = Portfolio.objects.all()
    data = {
        'title': 'Portfolio',
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio_home.html', data)


def display_projects_by_skill(request, skill_slug):
    skill = Skill.objects.get(slug=skill_slug)
    projects = Portfolio.objects.filter(skill=skill)
    data = {
        'title': 'Portfolio',
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio_home.html', data)


def project_detail(request, project_slug):
    project = Portfolio.objects.get(slug=project_slug)
    data = {
        'title': 'Project detail',
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', data)
