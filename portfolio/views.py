from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseNotFound
from django.core.mail import send_mail, BadHeaderError

from .models import Portfolio
from django.views.generic import ListView, CreateView

class PortfolioHome(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_home.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Portfolio'
        return context

# def portfolio_home(request):
#     projects = Portfolio.objects.all()
#     data = {
#         'title': 'Portfolio',
#         'projects': projects,
#     }
#     return render(request, 'portfolio/portfolio_home.html', data)

class SkillListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_home.html'
    context_object_name = 'projects'
    allow_empty = False

    def get_queryset(self):
        return Portfolio.objects.filter(skill__slug=self.kwargs['skill_slug'])


# def display_projects_by_skill(request, skill_slug):
#     skill = get_object_or_404(Skill, slug=skill_slug)
#     projects = Portfolio.objects.filter(skill=skill)
#     data = {
#         'title': 'Portfolio',
#         'projects': projects,
#     }
#     return render(request, 'portfolio/portfolio_home.html', data)


def project_detail(request, project_slug):
    project = get_object_or_404(Portfolio, slug=project_slug)
    data = {
        'title': 'Project detail',
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', data)

def contact(request):
    error = ''
    ad = {
        'first_name' : 'ggg',
        'last_name'  : 'kkk',
        'email_address': 'kira.moshkova@gmail.com',
        'message': 'mmm',

    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'esprit1C@yandex.ru', ['esprit1C@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Undesirable data')
            return redirect("home")
        else:
            error = 'Undesirable data'
    form = ContactForm(initial=ad)
    data = {
        'title': 'Contact',
        'form': form
    }
    return render(request, 'portfolio/contact.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
