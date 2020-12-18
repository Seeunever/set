from django.contrib import admin

# Register your models here.

# login/admin.py
from . import models
 
admin.site.register(models.User)