"""Tests for testing Users creation"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@example.com',
                                        password='password123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',
                                     password='password123')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='admin@example.com',
                                             password='password123')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_superuser(
                email='super@example.com', password='foo', is_superuser=False)