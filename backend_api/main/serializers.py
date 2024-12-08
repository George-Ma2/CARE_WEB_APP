from dataclasses import fields
from rest_framework import serializers # gets the model data and converts to JSON
from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 1

