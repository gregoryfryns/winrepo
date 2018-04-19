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
    # path('createfunc', views.create_profile, name='createfunc'),
    # path('submit', views.submit_create, name='submit_create'),
    # path('editfunc', views.edit_profile, name='editfunc'),
    # path('<int:pk>/submit', views.submit_edit, name='submit_edit'),
    path('list/<int:pk>/recommend', views.CreateRecommendation.as_view(), name='recommend'),
]
