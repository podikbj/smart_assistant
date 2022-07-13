from django.urls import path
from . import views

urlpatterns = [
    path('', views.links_home, name='links_home'),
    path('create_link', views.create_link, name='create_link'),
    path('category/<int:category_id>/', views.show_category, name='category'),
    path('<int:pk>', views.LinkDetailView.as_view(), name='link_details'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='category_details'),
    path('<int:pk>/update', views.LinkUpdateView.as_view(), name='link_update'),
    path('<int:pk>/delete', views.LinkDeleteView.as_view(), name='link_delete'),

]
