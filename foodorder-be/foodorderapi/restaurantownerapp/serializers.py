from rest_framework import serializers

from .models import Restaurant, Menu
from foodorderauthapp.serializers import RestaurantOwnerSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant_owner = RestaurantOwnerSerializer

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        restaurant_owner = validated_data.pop('restaurant_owner')
        restaurant = Restaurant.objects.create(**validated_data, restaurant_owner=restaurant_owner)
        print("New Restaurant added to DB")
        return restaurant

    def update(self, instance, validated_data):
        print("updating a restaurant...")
        restaurant_owner_data = validated_data.pop('restaurant_owner', None)

        instance.restaurant_name = validated_data.get('restaurant_name', instance.restaurant_name)
        instance.location = validated_data.get('location', instance.location)
        instance.cuisine = validated_data.get('cuisine', instance.cuisine)
        instance.save()
        return instance


class RestaurantMenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer

    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        restaurant = validated_data.pop('restaurant')
        menu = Menu.objects.create(**validated_data, restaurant=restaurant)
        print(f"New menu added to {restaurant}")
        return menu

    def update(self, instance, validated_data):
        print("updating a restaurant menu...")
        restaurant_data = validated_data.pop('restaurant', None)

        instance.dish_name = validated_data.get('dish_name', instance.dish_name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance




