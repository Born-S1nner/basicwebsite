from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateAccount
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(res):
  return render(res, "user/home.html", {})

def join(res):
  if res.method == 'POST':
    form = CreateAccount(res.POST)
    if form.is_valid():
      CU = form.cleaned_data['username']
      CP = form.cleaned_data['password']
      NA = Account(username=CU, password=CP)
      NA.save()
    return HttpResponseRedirect("/")
  else:
    form = CreateAccount()
  return render(res, "user/signup.html", {"form": form})

def LoginReunioun(res):
  return render(res, "user/login.html", {})

def Success(res):
  return render(res, "user/unlock.html", {})
