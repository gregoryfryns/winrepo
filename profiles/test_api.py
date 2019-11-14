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

    def setUp(self):
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve(self):
        profile_id = self.user.profile.pk
        response = self.client.get(reverse('profiles:profiles-detail', kwargs={'pk': profile_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'testcase')

    def test_profile_update_by_owner(self):
        test_data = {'institution': 'Test Uni', 'name': 'Test Name', 'keywords': 'Updated!'}
        profile_id = self.user.profile.pk
        response = self.client.put(reverse('profiles:profiles-detail', kwargs={'pk': profile_id}),
                                   test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        for k, v in test_data.items():
            self.assertEqual(data[k], v)

    def test_profile_update_by_other_user(self):
        profile_id = self.user.profile.pk
        random_user = User.objects.create_user(username='random', email='random@test.com', password='my_super_password')
        self.client.force_authenticate(user=random_user)

        response = self.client.put(reverse('profiles:profiles-detail', kwargs={'pk': profile_id}),
                                   {'institution': 'Test Uni', 'name': 'Random Name', 'keywords': 'Hacked!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecommendationViewSetTestClass(APITestCase):

    list_url = reverse('profiles:recommendations-list')

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='my_super_password')
        self.recommendation = Recommendation.objects.create(profile=self.user.profile,
                                                            reviewer_name='Test Reviewer',
                                                            reviewer_email='test@reviewer.com',
                                                            reviewer_institution='Test institution',
                                                            seen_at_conf=False,
                                                            comment='Awesome!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_recommendations_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recommendations_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
