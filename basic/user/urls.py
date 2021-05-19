from django.urls import path, include
from . import views

urlpatterns = [
  path("user/", include('django.contrib.auth.urls')),
  path("", views.home, name="home"),
  path("user/signup/", views.join, name="create")
]