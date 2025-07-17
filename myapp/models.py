from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
class Cars(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    desc = models.CharField()
    
    def __str__(self):
        return f"{self.name}"
    
class AvailableCars(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}"

class TrendingOffers(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    offers = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"