from rest_framework import viewsets
from bakery.models import Bakery
from bakery import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters


# Create your views here.
class BakeryViewSet(viewsets.ModelViewSet):
    """View or manage Country"""
    serializer_class = serializers.BakerySerializer
    queryset = Bakery.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'street']

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Create new Country"""
        serializer.save(user=self.request.user)
