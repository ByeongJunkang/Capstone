from itertools import product
from rest_framework import serializers
from .models import Kscholar,Interscholar

class ScholarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Kscholar
        fields = ('id','number','date','title','content','department',)

class InterestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Interscholar
        fields = ('user','product_option')

    