from unicodedata import name
from django.db import models

# Create your models here.
class Hypervisortabledb(models.Model):

    hypervisorIP = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    operatingSystem = models.CharField(max_length=100)
    ipAddress = models.CharField(max_length=16)
    state = models.CharField(max_length=20)