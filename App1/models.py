from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    name     = models.CharField(max_length=50) 
    age      = models.IntegerField()
    gender   = models.CharField(max_length=1)



