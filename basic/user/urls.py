from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("user/signup/", views.join, name="create"),
  path("user/login/", views.LoginReunioun, name="login"),
]