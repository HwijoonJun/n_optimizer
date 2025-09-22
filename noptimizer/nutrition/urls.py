from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nutrition.views import FoodViewSet, NutrientViewSet

# Initialize the API router and register endpoints for foods and nutrients
router = DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'nutrients', NutrientViewSet)

# URL patterns for the application:
# - 'admin/': Django admin interface
# - 'api/': API endpoints for foods and nutrients via DRF router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
