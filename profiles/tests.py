# from captcha.models import CaptchaStore
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# from .forms import CreateProfileModelForm
from .models import Country, Profile, Recommendation

default_profile = {
    'name': 'Test Profile',
    'position': 'Lecturer',
    'institution': 'Test institution',
    'grad_month': '06',
    'grad_year': '2010',
    'keywords': 'test one two',
    'is_public': True
}


class ModelsTests(TestCase):

    def test_new_user_new_profile(self):
        """
        If a new user is created, a linked profile should be created as well
        """
        email = 'test@user.com'
        user = User.objects.create_user(username='testuser', password='super-password', email=email)
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.profile.contact_email, email)

    def test_new_user_existing_profile(self):
        """
        If a new user is created, a linked profile should be created as well
        """
        email = 'existing@user.com'
        profile_settings = dict(default_profile)
        profile_settings['contact_email'] = email
        profile = Profile.objects.create(**profile_settings)

        user = User.objects.create_user(username='testuser', password='super-password', email=email)
        self.assertEqual(user.profile, profile)
        self.assertEqual(user.profile.user, user)


class ProfileDetailViewTests(TestCase):

    def setUp(self):
        self.country = Country.objects.create(code='USA',
                                              name='United States',
                                              is_under_represented=False)
        profile_settings = dict(default_profile)
        profile_settings['country'] = self.country

        self.profile = Profile.objects.create(**profile_settings)

        inactive_profile = dict(profile_settings)
        inactive_profile['is_public'] = False

        self.inactive = Profile.objects.create(**inactive_profile)

    def test_view_profile(self):
        """
        The detail view of a new profile can be accessed
        """
        url = reverse('profiles:detail', args=(self.profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_inactive(self):
        """
        The detail view of an inactive profile cannot be accessed
        """
        url = reverse('profiles:detail', args=(self.inactive.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_incorrect(self):
        """
        Asking for an incorrect profile ID returns an error 404
        """
        url = reverse('profiles:detail', args=(self.profile.id + 10,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recommendations_count(self):
        """
        All the recommendations are displayed in the profile detail page
        """
        recommendations_count = 5
        for i in range(recommendations_count):
            Recommendation.objects.create(profile=self.profile,
                                          reviewer_name=f'Reviewer {i}',
                                          reviewer_email=f'test{i}@test.com',
                                          seen_at_conf=False,
                                          comment='Test Comment')

        url = reverse('profiles:detail', args=(self.profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.context['profile']
                                 .recommendations
                                 .count(),
                         recommendations_count)

# TODO: disable captcha before testing
# class ProfileCreateViewTests(TestCase):

#     create_url = reverse('profiles:create')

#     def setUp(self):
#         self.country = Country.objects.create(code='USA',
#                                               name='United States',
#                                               is_under_represented=False)
    
#     def test_create_profile(self):
#         """
#         A profile can be created from the view, and the newly created profile is displayed
#         """
#         profile_settings = dict(default_profile)
#         profile_settings['country'] = self.country.id
#         profile_settings['contact_email'] = 'test@user.com'

#         response = self.client.post(self.create_url, profile_settings)
#         self.assertFormError(response, 'form', 'captcha', '')
#         self.assertEqual(response.status_code, 200)
#         new_profile = Profile.objects.filter(contact_email='test@user.com').first()
#         self.assertIsNotNone(new_profile)
#         self.assertURLEqual(response.redirect_chain, reverse('profiles:detail', args=(new_profile.id,)))

#     def test_create_profile_with_existing_email(self):
#         """
#         Form will not allow another user to be created with the same email address
#         """
#         email = 'test@user.com'
#         existing_profile = {'name': 'Existing User', 'institution': 'My institution', 'contact_email': email, 'country': self.country}
#         Profile.objects.create(**existing_profile)

#         profile_settings = dict(default_profile)
#         profile_settings['country'] = self.country.id
#         profile_settings['contact_email'] = email
#         response = self.client.post(self.create_url, profile_settings)
#         self.assertEqual(response.status_code, 200)
#         self.assertFormError(response, 'form', 'contact_email', 'This email address is already taken')


class ProfileListViewTests(TestCase):
    profiles = []
    index_url = reverse('profiles:index')

    def setUp(self):
        """
        Construct fake profiles
        """
        self.POSITION_CHOICES = Profile.get_position_choices()
        POSITION_CHOICES_IDS = [pos[0] for pos in self.POSITION_CHOICES]
        self.COUNTRIES = [
            Country.objects.create(code='USA',
                                   name='United States',
                                   is_under_represented=False),
            Country.objects.create(code='FRA',
                                   name='France',
                                   is_under_represented=False),
            Country.objects.create(code='VEN',
                                   name='Venezuela',
                                   is_under_represented=True)
        ]

        for i in range(1, 25):
            profile_settings = dict(default_profile)
            profile_settings['country'] = self.COUNTRIES[i % len(self.COUNTRIES)]
            profile_settings['name'] = f'User {i}'
            profile_settings['position'] = POSITION_CHOICES_IDS[i % len(POSITION_CHOICES_IDS)]
            self.profiles.append(Profile.objects.create(**profile_settings))

        for i in range(1, 5):
            profile_settings = dict(default_profile)
            profile_settings['country'] = self.COUNTRIES[i % len(self.COUNTRIES)]
            profile_settings['name'] = f'Inactive User {i}'
            profile_settings['is_public'] = False
            self.profiles.append(Profile.objects.create(**profile_settings))            

    def test_list_profiles(self):
        """
        The profiles list does not contain more than 20 profiles when it loads
        """
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(self.profiles), 20)
        self.assertEqual(len(response.context['profiles']), 20)

    def test_hide_private_profiles(self):
        """
        The profiles that are not public should not be displayed
        """
        page = 1
        response = self.client.get(f'{self.index_url}?page={page}')
        self.assertEqual(response.status_code, 200)
        while response.status_code == 200:
            for profile in response.context['profiles']:
                self.assertTrue(profile.is_public)
            page += 1
            response = self.client.get(f'{self.index_url}?page={page}')

    def test_filter_senior(self):
        """
        The query parameter senior=on should filter out the non-senior profiles
        """
        SENIOR_PROFILES = [pos[1] for pos in self.POSITION_CHOICES[4:]]

        senior_profiles_count = 0
        page = 1
        response = self.client.get(f'{self.index_url}?senior=on&page={page}')
        self.assertEqual(response.status_code, 200)
        while response.status_code == 200:
            for profile in response.context['profiles']:
                senior_profiles_count += 1
                self.assertIn(profile.get_position_display(), SENIOR_PROFILES)
            page += 1
            response = self.client.get(f'{self.index_url}?senior=on&page={page}')

        # get all results and see if we didn't miss any
        total_profiles_count = {'senior': 0, 'non-senior': 0}
        page = 1
        response = self.client.get(f'{self.index_url}?page={page}')
        self.assertEqual(response.status_code, 200)
        while response.status_code == 200:
            for profile in response.context['profiles']:
                if profile.get_position_display() in SENIOR_PROFILES:
                    total_profiles_count['senior'] += 1
                else:
                    total_profiles_count['non-senior'] += 1
            page += 1
            response = self.client.get(f'{self.index_url}?page={page}')

        self.assertEqual(total_profiles_count['senior'], senior_profiles_count)

    def test_filter_under_represented(self):
        """
        The query parameter ur=on should filter out the non under-represented countries
        """

        underrepresented_count = 0
        page = 1
        response = self.client.get(f'{self.index_url}?ur=on&page={page}')
        self.assertEqual(response.status_code, 200)
        while response.status_code == 200:
            for profile in response.context['profiles']:
                underrepresented_count += 1
                self.assertTrue(profile.country.is_under_represented)
            page += 1
            response = self.client.get(f'{self.index_url}?ur=on&page={page}')

        # get all results and see if we didn't miss any
        total_profiles_count = {'underrepresented': 0, 'other': 0}
        page = 1
        response = self.client.get(f'{self.index_url}?page={page}')
        self.assertEqual(response.status_code, 200)
        while response.status_code == 200:
            for profile in response.context['profiles']:
                if profile.country.is_under_represented:
                    total_profiles_count['underrepresented'] += 1
                else:
                    total_profiles_count['other'] += 1
            page += 1
            response = self.client.get(f'{self.index_url}?page={page}')

        self.assertEqual(total_profiles_count['underrepresented'], underrepresented_count)


class ProfileEmptyListViewTests(TestCase):
    index_url = reverse('profiles:index')

    def test_no_profile(self):
        """
        If no profiles exist, an appropriate message is displayed.
        """
        response = self.client.get(self.index_url)
        self.assertContains(response, 'No matching entries')
        self.assertQuerysetEqual(response.context['profiles'], [])


class StaticPagesTests(TestCase):
    def test_has_robots_file(self):
        response = self.client.get('/robots.txt')
        self.assertContains(response, 'User-agent')

    def test_has_sitemap(self):
        response = self.client.get(reverse('profiles:django.contrib.sitemaps.views.sitemap'))
        self.assertContains(response, '<urlset')

    def test_has_about_page(self):
        response = self.client.get(reverse('profiles:about'))
        self.assertContains(response, 'About')

    def test_has_faq_page(self):
        response = self.client.get(reverse('profiles:faq'))
        self.assertContains(response, 'Frequently')
