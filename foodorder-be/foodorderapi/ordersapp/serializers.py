from rest_framework import serializers

from .models import Order
from foodorderauthapp.serializers import CustomerSerializer
from restaurantownerapp.serializers import RestaurantMenuSerializer


# Orders Serializers
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer
    menu = RestaurantMenuSerializer

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'customer')

    def update(self, instance, validated_data):
        print("updating an order...")
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class OrderCreateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer
    menu = RestaurantMenuSerializer

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('status',)

    def create(self, validated_data):
        customer_obj = validated_data.pop('customer')
        menu_item = validated_data.pop('menu_item')
        user = self.context.get('user')
        customer = user.customer_account
        order = Order.objects.create(**validated_data, customer=customer, menu_item=menu_item)
        return order

