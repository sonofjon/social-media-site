from django.urls import path
from basic_app import views


urlpatterns = [
    path('', views.userprofile, name='userprofile'),
    path('about/', views.AboutView.as_view(), name='about'),
]