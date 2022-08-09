"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from bakery import views


router = DefaultRouter()
router.register('', views.BakeryViewSet, basename='bakeries')

app_name = 'bakeries'

urlpatterns = [
    path('', include(router.urls)),
]
