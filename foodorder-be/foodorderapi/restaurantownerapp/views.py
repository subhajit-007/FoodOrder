import json
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from foodorderauthapp.models import User, RestaurantOwner
from foodorderauthapp.serializers import RestaurantOwnerSerializer


class RestaurantOwnerListView(APIView):
    permission_classes = [IsAuthenticated]
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
