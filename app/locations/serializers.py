from rest_framework import serializers
from locations.models import Country, Province, City


class CitySerializer(serializers.ModelSerializer):
    bakeries = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        fields = [
            'name',
            'bakeries',
        ]


class ProvinceSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Province
        fields = [
            'country',
            'name',
            'cities',
        ]


class CountrySerializer(serializers.ModelSerializer):
    provinces = ProvinceSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'language',
            'language_short',
            'provinces',
        ]
