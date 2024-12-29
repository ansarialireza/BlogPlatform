from rest_framework import serializers
from .models import User,Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_staff', 'is_active', 'is_superuser', 'created_date', 'updated_date']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'image', 'description', 'created_date', 'updated_date']