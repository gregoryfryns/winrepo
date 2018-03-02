from django.urls import path

from . import views

app_name = 'viewlist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.UpdateProfile.as_view(), name='edit'),
    path('create', views.CreateProfile.as_view(), name='create'),
    path('<int:pk>/recommand', views.CreateRecommandation.as_view(), name='recommand'),
]