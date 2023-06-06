from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your models here.



class Bands(models.Model):

    band_name =  models.CharField(max_length=75)
    stage_name = models.CharField(max_length=25)
    day = models.CharField(max_length=20)


#class User(models.Model):


# name = models.CharField(max_length=30)


class Rating(models.Model):
    rating = models.CharField( max_length=2,null=True, blank= True)
    bands = models.ForeignKey('Bands', on_delete=models.CASCADE , null=True, blank=True)
    #User = models.ForeignKey('User',on_delete=models.RESTRICT)
    band_rater_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #User = models.ManyToManyField(User)
    #Bands = models.ManyToManyField(Bands)






