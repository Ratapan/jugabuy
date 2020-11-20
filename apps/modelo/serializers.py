from django.db.models import fields
from rest_framework import serializers
from apps.modelo.models import User

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','password']
