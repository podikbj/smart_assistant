from django.shortcuts import render


def portfolio_home(request):

    return render(request, 'portfolio/portfolio_home.html')

def create_project(request):
    return render(request, 'portfolio/create_project.html')
