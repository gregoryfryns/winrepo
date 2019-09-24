from django.test import TestCase
from django.urls import reverse

from .models import Profile, Country


default_user = {
    'name': 'Test Profile',
    'position': 'Lecturer',
    'institution': 'Test insitution',
    'grad_month': '06',
    'grad_year': '2010',
    'brain_structure': 'N',
    'modalities': 'EP',
    'methods': 'UV',
    'domains': 'CG',
    'keywords': 'test one two',
}


# Create your tests here.
class ProfileIndexViewTests(TestCase):
    def test_no_profile(self):
        """
        If no profiles exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No matching entries")
        self.assertQuerysetEqual(response.context['profiles'], [])


class ProfileDetailViewTests(TestCase):
    profile = None
    country = None

    def setUp(self):
        """
        Construct fake profiles
        """
        self.country = Country.objects.create(code='USA',
                                              name='United States',
                                              is_under_represented=False)
        user_settings = dict(default_user)
        user_settings['country'] = self.country

        self.profile = Profile.objects.create(**user_settings)

    def test_view_profile(self):
        """
        The detail view of a new profile can be accessed
        """
        url = reverse('profiles:detail', args=(self.profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ProfileListViewTests(TestCase):
    profiles = []
    country = None

    def setUp(self):
        """
        Construct fake profiles
        """
        self.country = Country.objects.create(code='USA',
                                              name='United States',
                                              is_under_represented=False)

        for i in range(1, 25):
            profile_settings = dict(default_user)
            profile_settings['country'] = self.country
            profile_settings['name'] = f'User {i}'
            self.profiles.append(Profile.objects.create(**profile_settings))

    def test_list_profiles(self):
        """
        The profiles list does not contain more than 20 profiles when it loads
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(self.profiles) > 20)
        self.assertEqual(len(response.context['profiles']), 20)
