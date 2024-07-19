from django.urls import path

from . import views


urlpatterns = [
    # Auth
    path('restaurant-owner/signup/', views.RestaurantOwnerRegistrationView.as_view(), name='restaurant-owner-registration'),
    path('customer/signup/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('token-verify/', views.TokenVerifyView.as_view(), name='token-verify'),
]
