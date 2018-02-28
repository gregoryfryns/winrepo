from django.urls import path

from . import views

app_name = 'viewlist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit'),
    path('<int:profile_id>/update', views.update_profile, name='update'),
    path('<int:profile_id>/recommend', views.recommend, name='recommend'),
    path('add', views.add_profile_form, name='add'),
    path('create', views.create_profile, name='create'),
]