from django.urls import path
from . import views
from .views import MyAppsHome, about, SignUpUser, LoginUser

urlpatterns = [
    path('', MyAppsHome.as_view(), name='home'),
    # path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),

]
