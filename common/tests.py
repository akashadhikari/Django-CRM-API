from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User

class UserTests(APITestCase):

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('get_post_user')
        data = {
            "username": "john",
            "email": "john@snow.com",
            "password": "you_know_nothing"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)