from email.headerregistry import Address
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122) 
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class PistolOrder(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gun_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    mode_info = models.CharField(max_length=100)
    date = models.DateField()

class RiflesOrder(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gun_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    mode_info = models.CharField(max_length=100)
    cost = models.CharField(max_length=20)
    date = models.DateField()

class ShotgunOrder(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gun_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    mode_info = models.CharField(max_length=100)
    cost = models.CharField(max_length=20)
    date = models.DateField()

class SniperOrder(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gun_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    mode_info = models.CharField(max_length=100)
    cost = models.CharField(max_length=20)
    date = models.DateField()

class SubMachineOrder(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    gun_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    mode_info = models.CharField(max_length=100)
    cost = models.CharField(max_length=20)
    date = models.DateField()