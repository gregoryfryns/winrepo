from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.ListProfiles.as_view(), name='index'),
    path('list/<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
    path('list/<int:pk>/edit', views.UpdateProfile.as_view(), name='edit'),
    path('list/create', views.CreateProfile.as_view(), name='create'),
    path('list/<int:pk>/recommend', views.CreateRecommendation.as_view(), name='recommend_profile'),
    path('list/recommend', views.CreateRecommendation.as_view(), name='recommend'),
    path('profiles-autocomplete', views.ProfilesAutocomplete.as_view(), name='profiles_autocomplete'),
    path('countries-autocomplete', views.CountriesAutocomplete.as_view(), name='countries_autocomplete'),
]
