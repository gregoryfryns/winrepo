from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles.api import views


router = DefaultRouter()
router.register('countries', views.RepresentedCountriesViewSet)
router.register('positions', views.TopPositionsViewSet)
router.register('profiles', views.ProfileViewSet, 'profiles')
router.register('recommendations', views.RecommendationViewSet, 'recommendations')

urlpatterns = [
    path('', include(router.urls)),
]
