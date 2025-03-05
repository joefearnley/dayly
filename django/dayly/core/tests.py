from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class HomeTest(TestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Get Started')
        self.assertContains(response, 'Log In')
