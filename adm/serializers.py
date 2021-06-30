from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'adress', 'contactNumber', 'category', 'email']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=True)
    
    class Meta:
        model = Service
        fields = ['name', 'price', 'peopleCount', 'period', 'description', 'company']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'category', 'company', 'status']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'nationality', 'birth_date', 'address', 'contact_number', 'number_id', 'issue_id', 'passport', 'email']

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(many=False)
    company = CompanySerializer(many=False)
    room = RoomSerializer(many=False)
    service = ServiceSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['customer', 'company', 'room', 'service', 'people_count', 'ocupation_date', 'leave_date', 'card_number', 'card_code']


