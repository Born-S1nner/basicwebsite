from django.shortcuts import render

# Create your views here.

def index(res):
  return render(res, "user/home.html", {})