from itertools import product
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )
    
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta: 
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"], 
            password = validated_data["password"],
            email = validated_data["email"],
            semester = validated_data["semester"],
            lastgpa = validated_data["lastgpa"],
            fullgpa = validated_data["fullgpa"],
            income = validated_data["income"],
            departments = validated_data["departments"],
            residence = validated_data["residence"]


          
            )
        return user
    
    
      