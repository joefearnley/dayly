import datetime
import random
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from faker import Faker
from entries.models import Entry


class EntriesBaseTest(APITestCase):
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

            self.default_date = datetime.datetime.now(datetime.timezone.utc)
            self.detault_slug = self.default_date.strftime('%Y-%m-%d') + '-' + str(random.choice(range(10000)))

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


class EntriesListTest(EntriesBaseTest):
    def setUp(self):
        super().setUp()

        self.entries_url = '/api/v1/entries/'
        self.entries = self.create_entrys(self.user, 5)

    def test_cannot_list_entries_without_authentication(self):
        response = self.client.get(self.entries_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_list_entries(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
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

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.entries_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.entries))

        for entry in self.entries:
            self.assertIn(entry.body, [e['body'] for e in response.data])

        for user_entry in other_user_entries:
            self.assertNotIn(user_entry.body, [e['body'] for e in response.data])


class ReadEntryTest(EntriesBaseTest):
    def setUp(self):
        super().setUp()

        self.entries_url = '/api/v1/entries/'
        self.entries = self.create_entrys(self.user, 1)

    def test_user_cannot_read_entry_without_authentication(self):
        entry = self.entries[0]
        response = self.client.get(f'{self.entries_url}{entry.id}/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_user_can_read_entry(self):
        entry = self.entries[0]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(f'{self.entries_url}{entry.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], entry.body)
        self.assertEqual(response.data['slug'], entry.slug)


class CreateEntryTest(EntriesBaseTest):
    def setUp(self):
        super().setUp()

        self.entries_url = '/api/v1/entries/'

    def test_user_cannot_create_entry_without_authentication(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_user_can_create_entry(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
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

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['body'], ['This field is required.'])

    def test_user_cannot_create_entry_without_date_published(self):
        post_data = {
            'body': self.faker.paragraph(),
            'slug': self.detault_slug,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['date_published'], ['This field is required.'])

    def test_user_cannot_create_entry_without_slug(self):
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.entries_url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Entry.objects.count(), 0)
        self.assertEqual(response.data['slug'], ['This field is required.'])


class UpdateEntryTest(EntriesBaseTest):
    def setUp(self):
        super().setUp()

        self.entries = self.create_entrys(self.user, 1)
        self.entries_url = '/api/v1/entries/'

    def test_user_cannot_update_entry_without_authentication(self):
        entry = self.entries[0]
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        response = self.client.put(f'{self.entries_url}{entry.id}/', data=post_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_user_can_update_entry(self):
        entry = self.entries[0]
        post_data = {
            'body': self.faker.paragraph(),
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(f'{self.entries_url}{entry.id}/', data=post_data)

        updated_entry = Entry.objects.get(id=entry.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_entry.body, post_data['body'])
        self.assertEqual(updated_entry.date_published, post_data['date_published'])
        self.assertEqual(updated_entry.slug, post_data['slug'])

    def test_user_cannot_update_entry_without_body(self):
        entry = self.entries[0]
        post_data = {
            'date_published': self.default_date,
            'slug': self.detault_slug,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(f'{self.entries_url}{entry.id}/', data=post_data)

        updated_entry = Entry.objects.get(id=entry.id)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(updated_entry.body, entry.body)
        self.assertEqual(response.data['body'], ['This field is required.'])

    def test_user_cannot_update_entry_without_date_published(self):
        entry = self.entries[0]
        post_data = {
            'body': self.faker.paragraph(),
            'slug': self.detault_slug,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(f'{self.entries_url}{entry.id}/', data=post_data)

        updated_entry = Entry.objects.get(id=entry.id)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(updated_entry.body, entry.body)
        self.assertEqual(response.data['date_published'], ['This field is required.'])


class DeleteEntryTest(EntriesBaseTest):
    def setUp(self):
        super().setUp()

        self.entries = self.create_entrys(self.user, 1)
        self.entries_url = '/api/v1/entries/'

    def test_user_cannot_delete_entry_without_authentication(self):
        entry = self.entries[0]
        response = self.client.delete(f'{self.entries_url}{entry.id}/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(len(response.data), 1)

    def test_user_can_delete_entry(self):
        entry = self.entries[0]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(f'{self.entries_url}{entry.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Entry.objects.count(), 0)

    def test_user_cannot_delete_entry_that_does_not_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(f'{self.entries_url}9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)

    def test_user_cannot_delete_entry_that_belongs_to_another_user(self):
        other_user = User.objects.create_user(
            username='testuser2',
            email='test_user_2@gmail.com',
            password='secret123',
            first_name='Jim',
            last_name='Doe',
        )

        other_user_entry = Entry.objects.create(
            body=self.faker.paragraph(),
            slug=self.detault_slug,
            date_published=self.default_date,
            user=other_user,
        )

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(f'{self.entries_url}{other_user_entry.id}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)
