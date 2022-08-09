from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError

from rest_framework import status
from rest_framework.test import APIClient

from locations.models import Country, Province, City

from locations.serializers import (
    CountrySerializer,
    ProvinceSerializer,
    CitySerializer
)


COUNTRIES_URL = reverse('locations:countries-list')
CITIES_URL = reverse('locations:cities-list')
PROVINCES_URL = reverse('locations:provinces-list')


def detail_url(country_id):
    """Create and return a recipe detail URL."""
    return reverse('locations:countries-detail', args=[country_id])


def create_country(user, **kwargs):
    """Create and return a sample Country"""
    defaults = {
        'name': 'USA',
        'language': 'american',
        'language_short': 'bru',
        'capital': 'Alaska',
        'dialing_code': 26
    }
    defaults.update(kwargs)

    country = Country.objects.create(user=user, **defaults)
    return country


class PublickCountryApiTest(TestCase):
    """Test Authenticated User, Read Only"""
    def setUp(self):
        self.client = APIClient()

    def test_get_not_admin_passes(self):
        res = self.client.get(COUNTRIES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_not_admin_fails(self):
        request = self.client.post(COUNTRIES_URL, {
            'name': 'Count', 'language': 'polish'})

        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_cities(self):
        res = self.client.get(CITIES_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminLoggedCountryApiTest(TestCase):
    """Test Authenticated User, Read Only"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
                                        email='admin@example.com',
                                        password='password123')
        self.client.force_authenticate(self.user)

    def test_retrieve_countries(self):
        create_country(user=self.user)

        res = self.client.get(COUNTRIES_URL)

        countries = Country.objects.all().order_by('-id')
        serializer = CountrySerializer(countries, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_by_user(self):
        create_country(user=self.user)

        res = self.client.get(COUNTRIES_URL)

        country = Country.objects.filter(user=self.user)
        serializer = CountrySerializer(country, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_unique_country_name(self):
        """Test that duplicate Country Names will raise IntegrityError"""
        with self.assertRaises(IntegrityError):
            create_country(user=self.user)
            create_country(user=self.user)

    def test_get_country_detail(self):
        """Test get single Country Details"""
        country = create_country(user=self.user)

        url = detail_url(country.id)
        res = self.client.get(url)

        serializer = CountrySerializer(country)

        self.assertEqual(res.data, serializer.data)

    def test_province_reqiere_country(self):
        """Test post a Province without country"""
        province_payload = {
            'name': 'Washington',
        }
        with self.assertRaises(IntegrityError):
            Province.objects.create(user=self.user, **province_payload)

    def test_create_province(self):
        """Test successfully post a Province"""
        country = create_country(user=self.user)

        payload = {
            'name': 'Washington',
            'country': 1,
        }

        res = self.client.post(PROVINCES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)




