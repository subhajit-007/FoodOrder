import json
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from foodorderauthapp.models import User, Customer
from foodorderauthapp.serializers import CustomerSerializer


class CustomerListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        data = json.loads(request.body)
        serializer = CustomerSerializer(customer, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        user = get_object_or_404(User, pk=customer.user.id)
        user.delete()
        print("Deleted Customer User: ", user)
        return Response(status=status.HTTP_204_NO_CONTENT)
