from django.db.models import Count

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView

from profiles.models import Country, Profile, Recommendation
from profiles.api.serializers import (CountrySerializer,
                                      ProfileSerializer,
                                      PositionsCountSerializer,
                                      RecommendationSerializer)

from profiles.api.permissions import IsAdminUserOrReadOnly


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


class ProfilesListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.all().order_by('-last_updated')
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all().order_by('-last_updated')
    serializer_class = ProfileSerializer
    # permission_classes = [IsSelfOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]


class RecommendationsListCreateAPIView(ListCreateAPIView):
    queryset = Recommendation.objects.all().order_by('-last_updated')
    serializer_class = RecommendationSerializer


class RecommendationRetrieveUpdateView(UpdateAPIView):
    queryset = Recommendation.objects.all().order_by('-last_updated')
    serializer_class = Recommendation
    permission_classes = [IsAdminUserOrReadOnly]
