# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clothing(models.Model):
    type = models.CharField(max_length=50)
    joy = models.BooleanField()
