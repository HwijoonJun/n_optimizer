from django.db import models
from django.db.models import Sum, Q

# Create your models here.

class Nutrient(models.Model):
    nutrient_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, null=True, blank=True)

class Food(models.Model):
    fdc_id = models.IntegerField(primary_key=True)
    data_type = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    food_category_id = models.IntegerField(null=True, blank=True)

    # Weight and calories should be calculated dynamically by summing relevant nutrients from related FoodNutrient instances.
    # Consider implementing this as a @property or method on the Food model, e.g.:
    # @property
    # def calories(self):
    #     # Sum the amount of the calorie nutrient from related FoodNutrient objects
    #     return sum(fn.amount for fn in self.nutrients.filter(nutrient__name='Calories'))
    @property
    def calories(self):
        #Sum of calories (kcal) from related FoodNutrient records.
        return (
            self.nutrients.filter(nutrient__name__icontains="Energy")
            .aggregate(total=Sum("amount"))
            .get("total")
            or 0
        )

    @property
    def weight(self):
        # Sum of weight-related nutrients ex. grams, miligrams)
        return (
            self.nutrients.filter(
                Q(nutrient__name__icontains="Weight") |
                Q(nutrient__name__icontains="Gram")
            )
            .aggregate(total=Sum("amount"))
            .get("total")
            or 0
        )

class FoodNutrient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='nutrients')
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    amount = models.FloatField()
    class Meta:
        unique_together = ('food', 'nutrient')