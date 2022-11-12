from itertools import product
from rest_framework import serializers
from .models import Kscholar

class ScholarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Kscholar
        fields = ('number','date','title','content','department',)

