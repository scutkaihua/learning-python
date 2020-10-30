from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __unicode__(self):
        return self.name
