from django.urls import path
from . import views
from .views import BlogHome, CityListView

urlpatterns = [
    path('', BlogHome.as_view(), name='blog_home'),
    # path('', views.blog_home, name='blog_home'),
    path('city/<int:city_id>/', CityListView.as_view(), name='city'),
    # path('city/<int:city_id>/', views.city, name='city'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),

]
