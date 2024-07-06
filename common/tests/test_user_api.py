"""
Tests for the user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('common:register')

def create_user(**params):
    """create and return a user."""
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the public features of the user API"""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_create_user_success(self):
        """Test creating a user is successful"""

        payload = {
            "first_name": "a",
            "last_name": "b",
            "email": "test11@gmail.com",
            "password": "a",
            "password_confirm": "a"
        }
        
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
    
    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""
        payload_api = {
            "first_name": "a",
            "last_name": "b",
            "email": "test11@gmail.com",
            "password": "a",
            "password_confirm": "a"
        }
        
        payload = {
            "first_name": "a",
            "last_name": "b",
            "email": "test11@gmail.com",
            "password": "a"
        }
        
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload_api)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)