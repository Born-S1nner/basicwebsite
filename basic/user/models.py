from django.db import models

# Create your models here.

class Account(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)

  def __str__(self):
    username = self.username
    password = self.password
    return "username: {}, password: {}".format(username, password)