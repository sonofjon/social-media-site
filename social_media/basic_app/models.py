from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class User(models.Model):

    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)

