from django.db.models import Count
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from profiles.models import Country, Profile, Recommendation
from profiles.api.serializers import (CountrySerializer,
                                      ProfileSerializer,
                                      PositionsCountSerializer,
                                      RecommendationSerializer)


class RepresentedCountriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.annotate(profiles_count=Count('profiles')) \
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


class ProfileListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.all().order_by('-last_updated')
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all().order_by('-last_updated')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RecommendationsListCreateAPIView(ListCreateAPIView):
    queryset = Recommendation.objects.all().order_by('-last_updated')
    serializer_class = RecommendationSerializer
