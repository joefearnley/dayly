from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


class UserApiTests(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'john_doe_123@gmail.com'
        self.password = 'secret123'
        self.first_name = 'John'
        self.last_name = 'Doe'

        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )

        self.users_url = '/api/v1/users/' 

    def test_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.users_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]['username'], self.username)
        self.assertEqual(response.data[0]['email'], self.email)
        self.assertEqual(response.data[0]['first_name'], self.first_name)
        self.assertEqual(response.data[0]['last_name'], self.last_name)

