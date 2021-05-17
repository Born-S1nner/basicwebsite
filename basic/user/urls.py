from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("user/signup/", views.join, name="join"),
  path("user/login/", views.join, name="return"),
]