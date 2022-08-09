"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from locations import views


router = DefaultRouter()
router.register('countries', views.CountryViewSet, basename='countries')
router.register('provinces', views.ProvinceViewSet, basename='provinces')
router.register('cities', views.CityViewSet, basename='cities')

app_name = 'locations'

urlpatterns = [
    path('', include(router.urls)),
]
