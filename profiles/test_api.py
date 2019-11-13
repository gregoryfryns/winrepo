import requests
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from rest_framework import status

from .api.serializers import (CountrySerializer, PositionsCountSerializer,
                              ProfileSerializer, RecommendationSerializer)
from .models import Profile, Recommendation


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'username': 'testcase',
            'email': 'test@test.com',
            'password1': 'my_super_password',
            'password2': 'my_super_password',
        }
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)