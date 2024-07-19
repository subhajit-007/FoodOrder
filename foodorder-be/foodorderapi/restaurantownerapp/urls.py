from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.RestaurantOwnerListView.as_view(), name='restaurant-list'),
    path('<int:pk>/details/', views.RestaurantOwnerDetailView.as_view(), name='restaurant-owner-detail'),
]
