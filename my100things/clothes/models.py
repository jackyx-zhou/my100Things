# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clothing(models.Model):
    CLOTHING_CATEGORIES = [
        ('Top', (
                ('shirt', 'shirt'),
                ('jacket', 'jacket'),
                ('hoodie', 'hoodie'),
                ('jumper', 'jumper'),
                ('other', 'other')
            )
        ),
        ('Trousers', (
                ('jeans', 'jeans'),
                ()
            )
        ),
        ('shorts', 'shorts'),
        ('underwear', 'underwear'),
        ('socks', 'socks'),
        ('accessory', 'accessory'),
        ('other', )
    ]
    type = models.CharField(max_length=50)
    joy = models.BooleanField()
