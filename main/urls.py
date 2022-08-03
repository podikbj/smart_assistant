from django.urls import path
from . import views
from .views import MyAppsHome, about

urlpatterns = [
    path('', MyAppsHome.as_view(), name='home'),
    # path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('signup/', RegisterUser.as_view(), name='signup'),

]
