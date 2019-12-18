from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('profiles', views.ProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),

    path('recommendations/',
         views.RecommendationCreateAPIView.as_view(),
         name='create-recommendation'),

    path('top-countries/',
         views.TopCountriesListAPIView.as_view(),
         name='top-countries'),

    path('countries-lookup/',
         views.CountriesLookupAPIView.as_view(),
         name='countries-lookup'),

    path('profiles-lookup/',
         views.ProfileLookupAPIView.as_view(),
         name='profiles-lookup'),

    path('top-positions/',
         views.TopPositionsListAPIView.as_view(),
         name='top-positions'),

    path('recommendations-sample/',
         views.RandomRecommendationsListAPIView.as_view(),
         name='random-recomendations'),
]
