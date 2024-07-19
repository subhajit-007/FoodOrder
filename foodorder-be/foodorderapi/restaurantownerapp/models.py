from django.db import models

from foodorderauthapp.models import RestaurantOwner


class Restaurant(models.Model):
    restaurant_owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE, related_name="restaurant_owner")
    restaurant_name = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=5000, blank=False)
    cuisine = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"id: {self.id} name:{self.restaurant_name}"


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")
    dish_name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, default="")
    price = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"id: {self.id} title:{self.dish_name}"
