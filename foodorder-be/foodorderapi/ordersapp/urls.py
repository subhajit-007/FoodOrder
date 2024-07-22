from django.urls import path
from . import views


urlpatterns = [
    # Orders
    path('', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('<int:pk>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('<int:pk>/manage/', views.OrderManageAPIView.as_view(), name='order-manage'),
    path('active/', views.ActiveOrderListAPIView.as_view(), name='active-orders'),
]
