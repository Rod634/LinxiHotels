from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'adress', 'contactNumber', 'category', 'email']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price', 'peopleCount', 'period', 'description']
