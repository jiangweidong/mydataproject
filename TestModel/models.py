from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=20)
class fllowers(models.Model):
    name=models.CharField(max_length=89)
