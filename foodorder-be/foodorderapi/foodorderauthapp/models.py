from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('restaurantowner', 'RestaurantOwner'),
        ('customer', 'Customer'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.id}. {self.username}"


class RestaurantOwner(models.Model):
    owner_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=500, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="restaurant_owner_account")

    def __str__(self):
        return f"{self.id}. {self.user.username}"


class Customer(models.Model):
    customer_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=500, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_account")

    def __str__(self):
        return f"{self.id}. {self.user.username}"
