from django.urls import path

from . import views

app_name = 'viewlist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.ProfileUpdate.as_view(), name='edit'),
    path('create', views.ProfileCreate.as_view(), name='create'),
    path('<int:profile_id>/recommend', views.recommend, name='recommend'),
]