from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(null=True)
    lastname = models.CharField(null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField( null=True)

    def __str__(self):
        return f" {self.firstname} {self.lastname} {self.phone} "