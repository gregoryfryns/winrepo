from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('countries', views.RepresentedCountriesViewSet)
router.register('positions', views.TopPositionsViewSet)
router.register('profiles', views.ProfileViewSet, basename='profiles')
router.register('recommendations', views.RecommendationViewSet, basename='recommendations')

urlpatterns = [
    path('', include(router.urls)),
]
