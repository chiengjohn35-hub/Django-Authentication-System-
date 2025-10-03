from django.db import models

# Create your models here.
class Student(models.Model):
    username =models.CharField(max_length=20)
    email = models.EmailField(null=False)
    password = models.IntegerField(null=False)


