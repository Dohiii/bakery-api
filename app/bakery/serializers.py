from rest_framework import serializers
from bakery.models import Bakery


class BakerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakery
        fields = [
            'name',
            'description',
            'specialization',
            'is_pizza',
            'is_cakes',
            'is_open_weekends',
            'street',
            'building_number',
            'flat_number',
            'zip_code',
            'latitude',
            'longitude',
            'city',
            'country',
            'province',
        ]
