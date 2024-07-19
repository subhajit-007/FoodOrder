from django.urls import path

from . import views


urlpatterns = [
    # path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    # path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),

    # Books
    # path('book-owners/', views.BookOwnerListView.as_view(), name='book-owner-list'),
    # path('book-owner/<int:pk>/', views.BookOwnerDetailView.as_view(), name='book-owner-detail'),

    # Auth
    path('restaurant-owner/signup/', views.RestaurantOwnerRegistrationView.as_view(), name='book-owner-registration'),
    path('customer/signup/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('token-verify/', views.TokenVerifyView.as_view(), name='token-verify'),
]
