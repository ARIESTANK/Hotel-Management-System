from rest_framework import serializers
from .models import Guests,Staffs,Rooms,Stays

class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'

class StaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stays
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['roomID', 'roomCode', 'building', 'accomodation', 'type', 'price', 'status']