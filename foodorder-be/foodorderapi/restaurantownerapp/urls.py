from django.urls import path
from . import views


urlpatterns = [
    path('owners/list/', views.RestaurantOwnerListView.as_view(), name='restaurant-owner-list'),
    path('list/', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('add/', views.RestaurantView.as_view(), name='create-restaurant'),
    path('<int:pk>/details/', views.RestaurantView.as_view(), name='restaurant-detail'),
    path('<int:pk>/details/', views.RestaurantOwnerDetailView.as_view(), name='restaurant-owner-detail'),
    path('<int:id>/menus/', views.RestaurantMenuListAPIView.as_view(), name='restaurant-menu-list'),
    path('menu/add/', views.MenuView.as_view(), name='create-restaurant-menu'),
    path('menu/<int:pk>/details/', views.MenuView.as_view(), name='restaurant-menu-detail'),
]
