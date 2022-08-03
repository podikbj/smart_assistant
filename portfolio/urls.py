from django.urls import path
from . import views
from .views import PortfolioHome, SkillListView

urlpatterns = [
    path('', PortfolioHome.as_view(), name='portfolio_home'),
    # path('', views.portfolio_home, name='portfolio_home'),
    path('contact/', views.contact, name='contact'),
    path('<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('skill/<slug:skill_slug>/', SkillListView.as_view(), name='display_projects_by_skill'),
    # path('skill/<slug:skill_slug>/', views.display_projects_by_skill, name='display_projects_by_skill'),

]
