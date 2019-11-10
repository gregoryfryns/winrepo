from django.db.models import Count

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView

from profiles.models import Country, Profile, Recommendation
from profiles.api.serializers import (CountrySerializer,
                                      ProfileSerializer,
                                      PositionsCountSerializer,
                                      RecommendationSerializer)

from profiles.api.permissions import ReadOnly, IsSelfOrReadOnly


class RepresentedCountriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.annotate(profiles_count=Count('profiles')) \
                              .filter(profiles_count__gt=0)
    serializer_class = CountrySerializer
    authentication_classes = []
    pagination_class = None


class TopPositionsViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []

    queryset = Profile.objects.filter(is_public=True) \
        .values('position') \
        .annotate(profiles_count=Count('id')) \
        .order_by('-profiles_count')
    serializer_class = PositionsCountSerializer
    pagination_class = None


class ProfilesListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.filter(is_public=True).order_by('-last_updated')
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.filter(is_public=True).order_by('-last_updated')
    serializer_class = ProfileSerializer
    permission_classes = [IsSelfOrReadOnly]


class RecommendationsListCreateAPIView(ListCreateAPIView):
    queryset = Recommendation.objects.all().order_by('-last_updated')
    serializer_class = RecommendationSerializer


class RecommendationRetrieveUpdateView(UpdateAPIView):
    queryset = Recommendation.objects.all().order_by('-last_updated')
    serializer_class = Recommendation
    permission_classes = [ReadOnly]
