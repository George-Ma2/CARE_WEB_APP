# from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from . import models

# Create your views here.
class VendorList(generics.ListCreateAPIView): # ListAPIView gets the data as a list
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView): # 
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]