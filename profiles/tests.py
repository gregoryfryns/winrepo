from django.test import TestCase
from django.urls import reverse

from .models import Profile


# Create your tests here.
def create_profile(name, position, institution, grad_date, country_id):
    return Profile.objects.create(name=name, position=position,
                                  institution=institution, grad_date=grad_date,
                                  country_id=country_id)


class ProfileIndexViewTests(TestCase):
    def test_no_profile(self):
        """
        If no profiles exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No profiles to show.")
        self.assertQuerysetEqual(response.context['profile_list'], [])


class QuestionDetailViewTests(TestCase):
    def test_view_profile(self):
        """
        The detail view of a new profile can be accessed
        """
        new_profile = create_profile('New Profile', 'Tester', 'My University',
                                     '2007-06-27', 24)
        url = reverse('profiles:detail', args=(new_profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
