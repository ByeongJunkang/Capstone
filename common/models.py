from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    semester = models.CharField(max_length=100)
    lastgpa = models.CharField(max_length=50)
    fullgpa = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    departments = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)

