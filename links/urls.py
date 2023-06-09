from django.urls import path
from . import views
from .views import LinksHome, CategoryListView, CreateLink

urlpatterns = [
    path('', LinksHome.as_view(), name='links_home'),
    # path('', views.links_home, name='links_home'),
    path('create_link/', CreateLink.as_view(), name='create_link'),
    # path('create_link/', views.create_link, name='create_link'),
    path('category/<int:category_id>/', CategoryListView.as_view(), name='category'),
    # path('category/<int:category_id>/', views.show_links_by_category, name='category'),
    path('<int:pk>/', views.LinkDetailView.as_view(), name='link_details'),
    path('<int:pk>/delete/', views.LinkDeleteView.as_view(), name='link_delete'),
    path('<int:pk>/update/', views.LinkUpdateView.as_view(), name='link_update'),
]
