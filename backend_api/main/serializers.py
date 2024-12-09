from dataclasses import fields
from rest_framework import serializers # gets the model data and converts to JSON
from . import models
from .models import Room

# class VendorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Vendor
#         fields=['id','user','address']

#     def __init__(self, *args, **kwargs):
#         super(VendorSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         self.Meta.depth = 1

# class VendorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Vendor
#         fields=['id','user','address']

#     def __init__(self, *args, **kwargs):
#         super(VendorDetailSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         self.Meta.depth = 1


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

class CreateRoomSerializer(serializers. ModelSerializer):
    class Meta:
        model = Room 
        fields = ('guest_can_pause', 'votes_to_skip')