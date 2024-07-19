import json

from .models import User, Customer, RestaurantOwner
from .serializers import UserSerializer, RestaurantOwnerSerializer, CustomerSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserRegistrationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantOwnerRegistrationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        serializer = RestaurantOwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRegistrationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        print("data ==> ", data)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)

            response_data = {
                'token': token.key,
                'username': user.username,
                'role': user.role,
            }

            # Restaurant Owner login
            if user.role == 'RestaurantOwner':
                book_owner = user.restaurant_owner_account  # As the related name is "book_owner_account"
                if book_owner is not None:
                    # Add RestaurantOwner data to the response data
                    restaurant_owner_data = RestaurantOwnerSerializer(book_owner).data
                    response_data['data'] = restaurant_owner_data
            elif user.role == 'customer':
                customer = user.customer_account
                if customer is not None:
                    # Add Restaurant Owner data to the response data
                    customer_data = CustomerSerializer(customer).data
                    response_data['data'] = customer_data

            return Response(response_data)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'detail': 'Successfully logged out.'})


class TokenVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"detail": "Token is valid"}, status=status.HTTP_200_OK)
