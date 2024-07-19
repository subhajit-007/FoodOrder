from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, RestaurantOwner, Customer


admin.site.register(User, UserAdmin)
admin.site.register(RestaurantOwner)
admin.site.register(Customer)
