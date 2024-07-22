import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer

from restaurantownerapp.models import Menu


# Orders Views

class OrderListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == 'customer':
            orders = Order.objects.filter(customer__user=user)
        elif user.role == 'restaurantowner':
            orders = Order.objects.filter(menu__restaurant__restaurant_owner__user=user)
        else:
            orders = Order.objects.none()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.role != 'customer':
            return Response({"detail": "Not authorized to place orders."}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderCreateSerializer(data=json.loads(request.body), context={'user': request.user})
        if serializer.is_valid():
            # menu = Menu.objects.get(id=serializer.validated_data['menu'].id)
            # if menu.quantity_aval < serializer.validated_data['quantity']:
            #     return Response({"detail": "Not enough stock available."}, status=status.HTTP_400_BAD_REQUEST)
            # menu.quantity_aval -= serializer.validated_data['quantity']
            # menu.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = request.user
        if user.role != 'restaurantowner':
            return Response({"detail": "Not authorized to manage orders."}, status=status.HTTP_403_FORBIDDEN)
        order = self.get_object(pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if order.menu.restaurant.restaurant_owner.user != user:
            return Response({"detail": "Not authorized to manage this order."}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderCreateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderManageAPIView(APIView):
    # permission_classes = [IsRestaurantOwner]

    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk, menu_item__restaurant__restaurant_owner__user=request.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = request.user
            if user.role == 'customer':
                return Response({"detail": "Not authorized to manage orders."}, status=status.HTTP_403_FORBIDDEN)

            order = Order.objects.get(pk=pk, menu_item__restaurant__restaurant_owner__user=request.user)
            serializer = OrderSerializer(order, data=json.loads(request.body), partial=True)
            if serializer.is_valid():
                serializer.save()
                print("update completed")
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class ActiveOrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(status__in=['pending', 'approved', 'shipped'])
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


