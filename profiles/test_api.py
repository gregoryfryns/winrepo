import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

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


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse('profiles:profiles-list')

    def setup(self):
        self.user = User.objects.create_user(username='testcase', email='test@test.com', password='my_super_password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        print(f'list url: {self.list_url}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profiles:profiles-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'testcase')

    def test_profile_update_by_owner(self):
        test_data = {'institution': 'Test Uni', 'name': 'Test Name', 'Keywords': 'Updated!'}
        response = self.client.put(reverse('profiles:profiles-detail', kwargs={'pk': 1}),
                                   test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content())
        for k, v in test_data:
            self.assertEqual(data[k], v)

    def test_profile_update_by_other_user(self):
        random_user = User.objects.create_user(username='random', email='random@test.com', password='my_super_password')
        self.client.force_authenticate(user=random_user)

        response = self.client.put(reverse('profiles:profiles-detail', kwargs={'pk': 1}),
                                   {'institution': 'Test Uni', 'name': 'Random Name', 'Keywords': 'Hacked!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
