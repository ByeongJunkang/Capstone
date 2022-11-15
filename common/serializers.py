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
            validated_data["username"], None, validated_data["password"])
        return user
    