from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'viewlist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.UpdateProfile.as_view(), name='edit'),
    path('create', views.CreateProfile.as_view(), name='create'),
    # path('createfunc', views.create_profile, name='createfunc'),
    # path('submit', views.submit_create, name='submit_create'),
    # path('editfunc', views.edit_profile, name='editfunc'),
    # path('<int:pk>/submit', views.submit_edit, name='submit_edit'),
    path('<int:pk>/recommend', views.CreateRecommendation.as_view(), name='recommend'),
]