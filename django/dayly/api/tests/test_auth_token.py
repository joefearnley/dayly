from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse


class AuthTokenTests(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'secret123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token_url = reverse('api-token-auth') 
        self.protected_url = '/api/entries/' 

    def test_token_created_on_login(self):
        response = self.client.post(self.token_url, {
            'username': self.username,
            'password': self.password
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_access_protected_view_without_token(self):
        response = self.client.get(self.protected_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_protected_view_with_token(self):
        token = Token.objects.create(user=self.user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = client.get(self.protected_url)

        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_token(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token invalidtoken123')

        response = client.get(self.protected_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
