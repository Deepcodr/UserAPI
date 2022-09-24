from django.forms import fields
from .models import User
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['UserID','Name','EmailID','Age','Address']