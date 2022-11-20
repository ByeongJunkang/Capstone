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
    



