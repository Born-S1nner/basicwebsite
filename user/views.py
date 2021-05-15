from django.shortcuts import HttpResponse

# Create your views here.

def index(res):
  return HttpResponse("<h1>Helloe</h1>")