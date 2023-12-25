from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from accounts.models import Provider

class TestProviderApi(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="lampNet", email="example@gmail.com",password="lampnet")
        self.data = {
            "name":"lampNet",
            "location":"juja",
            "phone_number":"+254757166234",
            "org_email":"example@gmail.com",
            "short_code":"1234567",
        }

        return super().setUp()

    def test_create_provider(self):
        """Ensure we can create provider """

        #endpoint
        url = reverse(viewname="create-provider")
  
        token = Token.objects.filter(user__email=self.user.email).first()
        headers = {"Authorization":f"Token {token.key}"}
        #   response
        response = self.client.post(url, data=self.data, headers=headers ,format="json")
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("provider", response.data.keys())

class TestUserApi(APITestCase):
    
    def test_create_user(self):
        """test creating user endpoint"""

        data = {
            "username":"lampNet",
            "email":"example@gmail.com",
            "password":"lampNet"
        }
        url = reverse("registration-list")
        response = self.client.post(url, data, format="json")
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(get_user_model().objects.count(),1)
        self.assertIn("token", response.data.keys())

class TestBandwidthApi(APITestCase):
    
    def test_create_bandwidth(self):
        pass
