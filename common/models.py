from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    semester = models.CharField(max_length=100,blank=True, null=True)
    lastgpa = models.CharField(max_length=50,blank=True, null=True)
    fullgpa = models.CharField(max_length=200,blank=True, null=True)
    income = models.CharField(max_length=200,blank=True, null=True)
    departments = models.CharField(max_length=200,blank=True, null=True)
    residence = models.CharField(max_length=200,blank=True, null=True)

