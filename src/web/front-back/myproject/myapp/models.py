from django.db import models

# Create your models here.
from __future__ import unicode_literals


class User(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
