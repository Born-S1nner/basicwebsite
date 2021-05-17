from django.shortcuts import render, HttpResponse

# Create your views here.
def home(res):
  return render(res, "user/home.html", {})

def join(res):
  return render(res, "user/signup.html", {})

def join(res):
  return render(res, "user/login.html", {})