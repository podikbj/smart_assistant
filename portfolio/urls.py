from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
    path('<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('skill/<slug:skill_slug>/', views.display_projects_by_skill, name='display_projects_by_skill'),

]
