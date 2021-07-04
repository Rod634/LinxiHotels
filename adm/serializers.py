from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ['pk', 'username']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'adress', 'contactNumber', 'category', 'email']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=True)
    
    class Meta:
        model = Service
        fields = ['pk', 'name', 'price', 'peopleCount', 'period', 'description', 'company']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = Room
        fields = ['pk', 'number', 'capacity', 'category', 'company', 'status', 'image_url']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ['pk', 'user', 'name', 'nationality', 'birth_date', 'address', 'contact_number', 'number_id', 'issue_id', 'passport', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        customer = Customer.objects.create(**validated_data)
        User.objects.create(customer=customer, **user_data)
        return customer

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(many=False)
    company = CompanySerializer(many=False)
    room = RoomSerializer(many=False)
    service = ServiceSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['pk', 'customer', 'company', 'room', 'service', 'people_count', 'ocupation_date', 'leave_date', 'card_number', 'card_code']


