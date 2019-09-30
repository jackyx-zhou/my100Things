# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from clothes.models import Clothing
from clothes.serializers import ClothingSerializer
from rest_framework import generics
class ClothingListCreate(generics.ListCreateAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
