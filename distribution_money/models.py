from django.db import models

class User(models.Model):
    money = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    inn = models.IntegerField(null=True)

# Create your models here.
