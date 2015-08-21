'''
Created on Aug 21, 2015

@author: hz
'''
from rest_framework import serializers
from djangular.models import Apple
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class AppleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apple
        fields = ('color', 'size', 'pk')