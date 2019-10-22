import re
import random

from functools import reduce
from operator import and_, or_

from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Count
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from dal.autocomplete import Select2QuerySetView
from rest_framework import viewsets

from .models import Profile, Recommendation, Country
from .forms import CreateProfileModelForm, RecommendModelForm
from .serializers import CountrySerializer, PositionsCountSerializer


class Home(ListView):
    template_name = 'profiles/home.html'
    context_object_name = 'recommendations_sample'
    model = Recommendation

    def get_queryset(self):
        sample = random.sample(
            list(Recommendation.objects.all()
                 .order_by('-id')[:100]),
            6)

        return sample


class ListProfiles(ListView):
    template_name = 'profiles/list.html'
    context_object_name = 'profiles'
    model = Profile
    paginate_by = 20

    def get_queryset(self):
        s = self.request.GET.get('s')
        is_underrepresented = self.request.GET.get('ur') == 'on'
        is_senior = self.request.GET.get('senior') == 'on'

        # create filter on search terms
        q_st = ~Q(pk=None)  # always true
        if s is not None:
            # split search terms and filter empty words (if successive spaces)
            search_terms = list(filter(None, s.split(' ')))

            for st in search_terms:
                st_regex = re.compile(f'.*{st}.*', re.IGNORECASE)

                # matching_positions = list(
                #   x[0]
                #   for x in Profile.get_position_choices()
                #   if st_regex.match(x[1]))
                matching_structures = list(
                    Q(brain_structure__contains=x[0])
                    for x
                    in Profile.get_structure_choices()
                    if st_regex.match(x[1]))
                matching_modalities = list(
                    Q(modalities__contains=x[0])
                    for x
                    in Profile.get_modalities_choices()
                    if st_regex.match(x[1]))
                matching_methods = list(
                    Q(methods__contains=x[0])
                    for x
                    in Profile.get_methods_choices()
                    if st_regex.match(x[1]))
                matching_domains = list(
                    Q(domains__contains=x[0])
                    for x
                    in Profile.get_domains_choices()
                    if st_regex.match(x[1]))

                st_conditions = [
                    Q(name__icontains=st),
                    Q(institution__icontains=st),
                    Q(position__icontains=st),
                    Q(brain_structure__icontains=st),
                    Q(country__name__icontains=st),
                    Q(keywords__icontains=st),
                 ] + matching_structures \
                   + matching_modalities \
                   + matching_methods \
                   + matching_domains

                q_st = and_(reduce(or_, st_conditions), q_st)

        #  create filter on under-represented countries
        if is_underrepresented:
            q_ur = Q(country__is_under_represented=True)
        else:
            q_ur = ~Q(pk=None)  # always true

        # create filter on senior profiles
        if is_senior:
            senior_profiles_keywords = ('Senior', 'Lecturer', 'Professor',
                                        'Director', 'Principal')
            # position must contain one of the words(case insensitive)
            q_senior = reduce(or_, (Q(position__icontains=x)
                                    for x
                                    in senior_profiles_keywords))
        else:
            q_senior = ~Q(pk=None)  # always true

        # apply filters
        profiles_list = Profile.objects \
                               .filter(q_st, q_ur, q_senior) \
                               .order_by('-publish_date')

        return profiles_list


class ProfileDetail(DetailView):
    model = Profile


class UpdateProfile(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = [
        'name',
        'email',
        'webpage',
        'institution',
        'country',
        'position',
        'grad_month',
        'grad_year',
        'brain_structure',
        'modalities',
        'methods',
        'domains',
        'keywords',
    ]
    success_message = "The profile for %(name)s was updated successfully"

    def get_success_url(self):
        return reverse('profiles:detail', args=(self.object.id,))


class CreateProfile(SuccessMessageMixin, CreateView):
    template_name = 'profiles/profile_form.html'
    form_class = CreateProfileModelForm
    success_message = "The profile for %(name)s was created successfully"

    def form_valid(self, form):
        # form.send_email()
        form.save()
        return super(CreateProfile, self).form_valid(form)

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.object.pk})


class CreateRecommendation(SuccessMessageMixin, FormView):
    template_name = 'profiles/recommendation_form.html'
    form_class = RecommendModelForm
    success_message = 'Your recommendation has been submitted successfully!'

    def form_valid(self, form):
        recommendation = form.save()
        self.profile_id = recommendation.profile.id
        return super(CreateRecommendation, self).form_valid(form)

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.profile_id})

    def get_initial(self):
        initial = super(CreateRecommendation, self).get_initial()
        profile_id = self.kwargs.get('pk')
        if profile_id is not None:
            profile = get_object_or_404(Profile, pk=profile_id)
            initial.update({'profile': profile})
        return initial


class ProfilesAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        profiles = Profile.objects.all()

        # If search terms in request, split each word and search for them
        # in name & institution
        if self.q:
            qs = ~Q(pk=None)  # always true
            search_terms = list(filter(None, self.q.split(' ')))
            for st in search_terms:
                qs = and_(or_(Q(name__icontains=st),
                              Q(institution__icontains=st)), qs)

            profiles = profiles.filter(qs)

        return profiles


class CountriesAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        countries = Country.objects.all()

        # If search terms in request, split each word and search for them
        # in name & institution
        if self.q:
            qs = ~Q(pk=None)  # always true
            search_terms = list(filter(None, self.q.split(' ')))
            for st in search_terms:
                qs = and_(Q(name__icontains=st), qs)

            countries = countries.filter(qs)

        return countries


class RepresentedCountriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.annotate(profiles_count=Count('profile')) \
                              .filter(profiles_count__gt=0)
    serializer_class = CountrySerializer
    authentication_classes = []


class TopPositionsViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []

    queryset = Profile.objects.all() \
        .values('position') \
        .annotate(profiles_count=Count('id')) \
        .order_by('-profiles_count')
    serializer_class = PositionsCountSerializer
