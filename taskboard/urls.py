from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskboard_home, name='taskboard_home'),
    path('create_task', views.create_task, name='create_task'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task_details'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
]