from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from bakery.models import Bakery
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

BAKERY_URL = reverse('bakeries:bakeries-list')


class PublicBakeryModel(TestCase):
    def setUp(self):
        self.bakery = baker.make(Bakery)

    def test_get_auth_not_required(self):
        """Not authorised user can GET bakeries"""
        res = self.client.get(BAKERY_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_not_authed_user_fails(self):
        """Not authorised user can not POST"""
        request = self.client.post(BAKERY_URL, {
            'name': 'Name',
            'street ': 'Gorna Wilda',
            'building_number ': 21,
            'flat_number ': 11,
            'zip_code ': '12-244',
            'city': 1,
            'country': 1,
            'province': 1,
        })

        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)


class LoggedInBakeryModel(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password123')
        self.client.force_authenticate(self.user)
        self.bakery = baker.make(Bakery)
        self.bakery2 = baker.make(Bakery)
        self.bakery.user = self.user
        self.bakery2.user = self.user

    def test_authorised_user(self):
        """Not authorised user can not POST"""
        request = self.client.post(BAKERY_URL, {
            'name': 'Name',
            'street ': 'Gorna Wilda',
            'building_number ': 21,
            'flat_number ': 11,
            'zip_code ': '12-244',
            'city': 1,
            'country': 1,
            'province': 1,
        })

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
