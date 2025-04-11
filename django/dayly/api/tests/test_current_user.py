from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status


class CurrentUserApiTests(APITestCase):
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

        self.token = Token.objects.create(user=self.user)
        self.token.save()

        self.users_url = '/api/v1/users/'

    def test_current_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.users_url + 'current/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)        

        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['email'], self.email)
        self.assertEqual(response.data['first_name'], self.first_name)
        self.assertEqual(response.data['last_name'], self.last_name)

    def test_super_user_only_sees_current_user(self):
        super_user = self.user
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()

        non_super_user = User.objects.create_user(
            username='non_super_user',
            email='john.doe32@gmail.com',
            password='secret123',
            first_name='John',
            last_name='Doe',
        )

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.users_url + 'current/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['email'], self.email)
        self.assertEqual(response.data['first_name'], self.first_name)
        self.assertEqual(response.data['last_name'], self.last_name)

        self.assertNotIn(non_super_user.username, response.data)
        self.assertNotIn(non_super_user.email, response.data)
        self.assertNotIn(non_super_user.first_name, response.data)
        self.assertNotIn(non_super_user.last_name, response.data)
