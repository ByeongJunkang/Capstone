from django.contrib.auth.models import AbstractUser
from django.db import models




class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.subject



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()





class Kscholar(models.Model):

    number = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    attachment_url = models.TextField(blank=True, null=True)
    attachment_content = models.TextField(blank=True, null=True)
    current_url = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)


class Interscholar(models.Model):
    user           = models.ForeignKey('common.User', on_delete=models.CASCADE)
    product_option = models.ForeignKey('Kscholar', on_delete=models.CASCADE)
    


class Berta(models.Model) :
    number = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date = models.TextField()
    content = models.TextField()
    content_revised = models.TextField()
    attachment_url = models.CharField(max_length=400, blank=True, null=True)
    attachment_content = models.TextField(blank=True, null=True)
    content_url = models.CharField(max_length=400)
    department = models.CharField(max_length=100)
    con_age = models.CharField(max_length=200, blank=True, null=True)
    con_bef_score = models.CharField(max_length=200, blank=True, null=True)
    con_total_score = models.CharField(max_length=200, blank=True, null=True)
    con_income = models.CharField(max_length=200, blank=True, null=True)
    con_major = models.CharField(max_length=200, blank=True, null=True)
    con_where = models.CharField(max_length=200, blank=True, null=True)
    con_end_date = models.CharField(max_length=200, blank=True, null=True)
    con_special = models.CharField(max_length=200, blank=True, null=True)

    
