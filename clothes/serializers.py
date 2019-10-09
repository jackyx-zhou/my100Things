from rest_framework import serializers
from clothes.models import Clothing

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ('id', 'type', 'description', 'colour', 'joy')
