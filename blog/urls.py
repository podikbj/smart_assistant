from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('city/<int:city_id>/', views.city, name='city'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),

]
