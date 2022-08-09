from rest_framework import viewsets
from locations.models import Country, Province, City
from locations import serializers
from rest_framework.permissions import AllowAny, IsAdminUser


# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    """View or manage Country"""
    serializer_class = serializers.CountrySerializer
    queryset = Country.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Create new Country"""
        serializer.save(user=self.request.user)

class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProvinceSerializer
    queryset = Province.objects.all()
    permission_classes = [IsAdminUser, ]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Create new Country"""
        serializer.save(user=self.request.user)


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CitySerializer
    queryset = City.objects.all()
    permission_classes = [IsAdminUser, ]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Create new Country"""
        serializer.save(user=self.request.user)
