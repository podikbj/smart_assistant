from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import MyApps
from django.views.generic import ListView, CreateView


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'main/signup.html'
#     success_url = reverse_lazy('signup')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Sign up")
#         return dict(list(context.items()) + list(c_def.items()))

class MyAppsHome(ListView):
    model = MyApps
    template_name = 'main/index.html'
    context_object_name = 'elements'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Smart assistant'
        return context

    def get_queryset(self):
        return MyApps.objects.order_by('id')


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

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
