import re 
from typing_extensions import NotRequired, Required
from unicodedata import name
from django.db import models
from pkg_resources import require

# Create your models here.
class Hypervisortabledb(models.Model):

    id = models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name ='ID',  blank=True)
    hypervisorIP = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    operatingSystem = models.CharField(max_length=100)
    ipAddress = models.CharField(max_length=16, null=True, blank=True, default='')
    state = models.CharField(max_length=20)
