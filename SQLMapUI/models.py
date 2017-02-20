from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.usernaxme

class PortCrack(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status   = models.CharField(max_length=10)
    type     = models.CharField(max_length=10)
    log      = models.CharField(max_length=10)
    progress = models.TextField()