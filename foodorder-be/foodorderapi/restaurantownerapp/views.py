import json
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import RestaurantSerializer, RestaurantMenuSerializer
from .models import Restaurant, Menu
from foodorderauthapp.models import User, RestaurantOwner
from foodorderauthapp.serializers import RestaurantOwnerSerializer


class RestaurantView(APIView):

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RestaurantSerializer(data=json.loads(request.body), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        data = json.loads(request.body)
        serializer = RestaurantSerializer(restaurant, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        print("Deleted restaurant: ", restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantListView(APIView):
    """List down all the restaurants"""
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantMenuListAPIView(APIView):
    """Get all menu item of the requested restaurant"""
    def get(self, request, id):
        try:
            restaurant = Restaurant.objects.get(pk=id)
        except Restaurant.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        menus = restaurant.menu.all()
        serializer = RestaurantMenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuView(APIView):
    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = RestaurantMenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RestaurantMenuSerializer(data=json.loads(request.body), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        data = json.loads(request.body)
        serializer = RestaurantMenuSerializer(menu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        print("Deleted menu: ", menu)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantOwnerListView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        restaurant_owners = RestaurantOwner.objects.all()
        serializer = RestaurantOwnerSerializer(restaurant_owners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantOwnerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        restaurant_owner = get_object_or_404(RestaurantOwner, pk=pk)
        serializer = RestaurantOwnerSerializer(restaurant_owner)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        restaurant_owner = get_object_or_404(RestaurantOwner, pk=pk)
        data = json.loads(request.body)
        serializer = RestaurantOwnerSerializer(restaurant_owner, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant_owner = get_object_or_404(RestaurantOwner, pk=pk)
        user = get_object_or_404(User, pk=restaurant_owner.user.id)
        user.delete()
        print("Deleted Book-Owner User: ", user)
        return Response(status=status.HTTP_204_NO_CONTENT)
