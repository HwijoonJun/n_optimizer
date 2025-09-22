from rest_framework import serializers
from .models import Food, Nutrient, FoodNutrient

class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'

class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer()
    class Meta:
        model = FoodNutrient
        fields = ['nutrient', 'amount']

class FoodSerializer(serializers.ModelSerializer):
    nutrients = FoodNutrientSerializer(many=True)
    class Meta:
        model = Food
        fields = '__all__'
