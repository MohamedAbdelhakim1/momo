from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
   

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'


class ImageUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()    





class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)

class ChatResponseSerializer(serializers.Serializer):
    bot_response = serializers.CharField()                    