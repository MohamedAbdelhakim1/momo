from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class Food1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Food1
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'