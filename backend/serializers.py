from rest_framework import serializers
from .models import Guests,Staffs

class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'
