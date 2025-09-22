from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Food, Nutrient
from .serializers import FoodSerializer, NutrientSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class NutrientViewSet(viewsets.ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer
