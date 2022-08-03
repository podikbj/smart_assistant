from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskboard/task_details.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'taskboard/create_task.html'
    form_class = TaskForm

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'taskboard/delete_task.html'
    success_url = '/taskboard/'

class TODOHome(ListView):
    model = Task
    template_name = 'taskboard/taskboard_home.html'
    # context_object_name = 'elements'
    paginate_by = 8  # how may items per page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TODO'
        return context

    def get_queryset(self):
            return Task.objects.order_by('deadline_day', 'deadline_time')

# def taskboard_home(request):
#     tasks = Task.objects.order_by('deadline_day', 'deadline_time')
#
#     data = {
#         'title': 'TODO',
#         'elements': tasks,
#     }
#     return render(request, 'taskboard/taskboard_home.html', data)

def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskboard_home')
        else:
            error = 'Undesirable data'
    form = TaskForm()
    data = {
        'form': form,
        'title': 'Create a new task',
        'error': error,
    }
    return render(request, 'taskboard/create_task.html', data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
