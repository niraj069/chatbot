from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
