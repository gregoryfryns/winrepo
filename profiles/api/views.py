from django.db.models import Q, Count
from rest_framework import viewsets

from profiles.models import Country, Profile
from profiles.api.serializers import CountrySerializer, PositionsCountSerializer


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
