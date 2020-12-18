# login/models.py
 
from django.db import models
import MySQLdb
import steam.settings


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32,default='root')

class Steam(models.Model):
    game_id = models.CharField(max_length=100, blank=True, null=True)
    game_name = models.CharField(max_length=100, blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    released_time = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    find_time = models.CharField(max_length=100, blank=True, null=True)

