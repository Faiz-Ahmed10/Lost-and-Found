from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
      user = models.CharField(max_length=128,blank=True)

      email = models.EmailField(blank=True, unique=True)

      password = models.CharField(max_length=128, blank=True)

        # Use a PositiveIntegerField for a unique ID with a maximum of 10 digits
    #   id = models.PositiveIntegerField(primary_key=True, unique=True, editable=False)
      id = models.CharField(primary_key=True,max_length=200)
      def __str__(self):
        return self.user
      
class UplodedItems(models.Model):
    ItemName = models.CharField(max_length=128,blank=False)
    Place = models.CharField(max_length=128,blank=False)
    Time = models.TimeField(max_length=128)
    Date = models.DateField(blank=True)
    Description = models.CharField(blank=False)
    Email = models.EmailField(blank=True)
    Image= models.ImageField(upload_to='',null=True,blank=True)
    def __str__(self):
        return self.ItemName