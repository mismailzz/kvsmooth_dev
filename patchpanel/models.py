from django.db import models

# Create your models here.
class Uploadvmpatchdb(models.Model):
    id = models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name ='ID',  blank=True)
    #hypervisorIP = models.CharField(max_length=16)
    script = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    