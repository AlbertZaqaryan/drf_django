from django.shortcuts import render
from .models import Car, Category
from .serializers import CarSerializer, CategorySerializer
from rest_framework import viewsets
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
