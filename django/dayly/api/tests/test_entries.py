import datetime
import random
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from faker import Faker
from entries.models import Entry


class EntriesListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test_user_1@gmail.com',
            password='secret123',
            first_name='John',
            last_name='Doe',
        )

        self.faker = Faker()

        self.token = Token.objects.create(user=self.user)
        self.token.save()

        self.entries = self.create_entrys(self.user, 3)
        self.entries_url = '/api/v1/entries/'

    def create_entrys(self, user, count):
        for i in range(count):
            date_published = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(weeks=i)
            slug = date_published.strftime('%Y-%m-%d') + '-' + str(random.choice(range(10000)))
            Entry.objects.create(
                body=self.faker.paragraph(),
                slug=slug,
                date_published=date_published,
                user=user,
            )

        return Entry.objects.filter(user=user)

    def test_cannot_list_entries_without_authentication(self):
        response = self.client.get(self.entries_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_list_entries(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.entries_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.entries))

        for entry in self.entries:
            self.assertIn(entry.body, [e['body'] for e in response.data])

    def test_user_only_sees_own_entries(self):
        self.other_user = User.objects.create_user(
            username='testuser2',
            email='test_user_2@gmail.com',
            password='secret123',
            first_name='Jim',
            last_name='Doe',
        )

        other_user_entries = self.create_entrys(self.other_user, 2)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.entries_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.entries))

        for entry in self.entries:
            self.assertIn(entry.body, [e['body'] for e in response.data])

        for user_entry in other_user_entries:
            self.assertNotIn(user_entry.body, [e['body'] for e in response.data])


class CreateEntryTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test_user_1@gmail.com',
            password='secret123',
            first_name='John',
            last_name='Doe',
        )

        self.faker = Faker()
        self.default_date = datetime.datetime.now(datetime.timezone.utc)
        self.detault_slug = self.default_date.strftime('%Y-%m-%d') + '-' + str(random.choice(range(10000)))
        self.entries_url = '/api/v1/entries/'

    def test_user_cannot_create_entry_without_authentication(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_user_can_create_entry(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        new_entry = Entry.objects.filter(user=self.user).first()

        self.assertEqual(new_entry.body, post_data['body'])
        self.assertEqual(new_entry.date_published, post_data['date_published'])

    def test_user_cannot_create_entry_without_body(self):
        post_data = {
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['body'], ['This field is required.'])

    def test_user_cannot_create_entry_without_date_published(self):
        post_data = {
            'body': self.faker.paragraph(),
            'slug': self.detault_slug,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['date_published'], ['This field is required.'])

    def test_user_cannot_create_entry_without_slug(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['slug'], ['This field is required.'])

