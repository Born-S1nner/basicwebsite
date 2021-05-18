from django.shortcuts import render, HttpResponse
from .forms import CreateAccount

# Create your views here.
def home(res):
  return render(res, "user/home.html", {})

def join(res):
  return render(res, "user/signup.html", {})

def login(res):
  return render(res, "user/login.html", {})
