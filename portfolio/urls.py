from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('project_detail', views.project_detail, name='project_detail'),
]