from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('city/<int:cityid>/', views.city, name='city'),
    path('<int:blogid>/', views.blog_details, name='blog_details'),

]
