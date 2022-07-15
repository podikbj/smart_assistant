from django.shortcuts import render, redirect
from . models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView

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

def taskboard_home(request):
    tasks = Task.objects.order_by('deadline_day', 'deadline_time')

    data = {
        'title': 'Taskboard',
        'elements': tasks,
    }
    return render(request, 'taskboard/taskboard_home.html', data)

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
