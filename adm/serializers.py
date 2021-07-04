from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['pk', 'username']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=True)
    
    class Meta:
        model = Service
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = Room
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    # user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = '__all__'

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     customer = Customer.objects.create(**validated_data)
    #     User.objects.create(customer=customer, **user_data)
    #     return customer

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'

