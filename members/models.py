from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Country(models.Model):
  Countrycode = models.CharField(max_length=255)
  Countryname = models.CharField(max_length=255)
  

class State(models.Model):
  Country=models.ForeignKey(Country,on_delete=models.CASCADE)
  Statecode = models.CharField(max_length=255)
  Statename = models.CharField(max_length=255)

class City(models.Model):
  State=models.ForeignKey(State,on_delete=models.CASCADE)
  Citycode = models.CharField(max_length=255)
  Cityname = models.CharField(max_length=255)
 
class Member(AbstractBaseUser):
  UserName = models.CharField(max_length=255,unique= True)
  Password = models.CharField(max_length=255)
  FirstName = models.CharField(max_length=255)
  LastName = models.CharField(max_length=255)

  
    