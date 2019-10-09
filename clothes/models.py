# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clothing(models.Model):
    CLOTHING_CATEGORIES = [
        ('Top', (
                ('shirt', 'shirt'),
                ('t-shirt', 't-shirt'),
                ('jacket', 'jacket'),
                ('hoodie', 'hoodie'),
                ('jumper', 'jumper'),
                ('other', 'other')
            )
        ),
        ('Trousers', (
                ('jeans', 'jeans'),
                ('joggers', 'joggers'),
                ('other','other')
            )
        ),
        ('shorts', 'shorts'),
        ('underwear', 'underwear'),
        ('socks', 'socks'),
        ('accessory', 'accessory'),
        ('other', 'other'),
    ]
    type = models.CharField(max_length=15, choices=CLOTHING_CATEGORIES)
    description = models.CharField(max_length=50, blank=True)
    colour = models.CharField(max_length=6, blank=True)
    joy = models.BooleanField()
