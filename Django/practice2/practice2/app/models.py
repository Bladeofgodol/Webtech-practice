from django.db import models
from django.forms import CharField

class hobby(models.Model):
    hobby_type = ()
    name = models.CharField( max_length=12)
    type = models.CharField(max_length=12,blank=True)
    
# Create your models here.
