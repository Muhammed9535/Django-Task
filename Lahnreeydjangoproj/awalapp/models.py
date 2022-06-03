from email.headerregistry import Address
from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=2)
    Address = models.CharField(max_length=23)

        

class Country(models.Model):
    name = models.CharField(max_length=2)
    