from django.shortcuts import render
from .models import Car, Category
from .serializers import CarSerializer, CategorySerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticatedOrReadOnly 
from rest_framework.permissions import BasePermission , SAFE_METHODS
from cart.cart import Cart
from rest_framework.generics import (
    ListAPIView , ListCreateAPIView , 
    DestroyAPIView , RetrieveAPIView , 
    UpdateAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
)



# Create your views here.
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (request.user and
            request.user.is_staff)
        )


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAdminOrReadOnly,)



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarListAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer