import re

from functools import reduce
from operator import and_, or_

from django.db.models import Count, Q

from rest_framework import mixins
from rest_framework import viewsets

from profiles.models import Country, Profile, Recommendation
from profiles.api.serializers import (CountrySerializer,
                                      ProfileSerializer,
                                      PositionsCountSerializer,
                                      RecommendationSerializer)

from profiles.api.permissions import IsOwnProfileOrReadOnly


class RepresentedCountriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.annotate(profiles_count=Count('profiles')) \
                              .filter(profiles_count__gt=0)
    serializer_class = CountrySerializer
    authentication_classes = []
    pagination_class = None


class TopPositionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = []

    queryset = Profile.objects.filter(is_public=True) \
                      .values('position') \
                      .annotate(profiles_count=Count('id')) \
                      .order_by('-profiles_count')
    serializer_class = PositionsCountSerializer
    pagination_class = None


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnProfileOrReadOnly]

    def get_queryset(self):
        queryset = Profile.objects
        q_st = Q(is_public=True)

        s = self.request.query_params.get('s', None)
        if s is not None:
            search_terms = list(filter(None, s.split(' ')))

            for st in search_terms:
                st_regex = re.compile(f'.*{st}.*', re.IGNORECASE)

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

        ur = self.request.query_params.get('under-represented', None)
        q_ur = ~Q(pk=None)  # always true
        if ur is not None:
            q_ur = Q(country__is_under_represented=True)

        is_senior = self.request.query_params.get('senior', None)
        q_senior = ~Q(pk=None)  # always true
        if is_senior is not None:
            senior_profiles_keywords = ('Senior', 'Lecturer', 'Professor',
                                        'Director', 'Principal')
            # position must contain one of the words(case insensitive)
            q_senior = reduce(or_, (Q(position__icontains=x)
                                    for x
                                    in senior_profiles_keywords))

        return queryset.filter(q_st, q_ur, q_senior).order_by('-last_updated')


class RecommendationViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        queryset = Recommendation.objects.all()
        profile_id = self.request.query_params.get('profile', None)
        if profile_id is not None:
            queryset = queryset.filter(profile__pk=profile_id)

        return queryset.order_by('-last_updated')
