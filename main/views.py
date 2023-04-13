from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginUserForm, SignUpUserForm
from .utils import DataMixin
from .models import MyApps
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView

class MyAppsHome(ListView):
    model = MyApps
    template_name = 'main/index.html'
    context_object_name = 'elements'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Smart assistant'
        context['is_authenticated'] = False
        if self.request.user.is_authenticated:
            context['is_authenticated'] = True
        return context

    def get_queryset(self):
        return MyApps.objects.order_by('id')


class SignUpUser(DataMixin, CreateView):
    form_class = SignUpUserForm
    template_name = 'main/sign_up.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        return dict(list(context.items()) + list(c_def.items()))



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


# def index(request):
#     my_apps = MyApps.objects.order_by('id')
#     data = {
#         'title': 'Smart assistant',
#         'elements': my_apps,
#
#     }
#     return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'ABOUT',
    }
    return render(request, 'main/about.html', data)

def login(request):
    data = {
        'title': 'Login',
    }
    return render(request, 'main/about.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
