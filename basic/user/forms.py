from django import forms
from .models import Account

class CreateAccount(forms.Form):
  username = forms.CharField(label="username", max_length=300)
  password = forms.CharField(label="password", max_length=200)