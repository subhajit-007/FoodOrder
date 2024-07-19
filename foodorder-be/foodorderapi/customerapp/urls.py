from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name='customer-list'),
    path('<int:pk>/details/', views.CustomerDetailView.as_view(), name='customer-detail'),
]
