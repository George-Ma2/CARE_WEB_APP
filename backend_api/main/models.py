from django.db import models
from django.contrib.auth.models import User
import string
import random


# # Create your models here.
# class Vendor(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE) # CASCADE allows to delete all the data of the user when deleting the user
#     address = models.TextField(null=True) # user can leave the field in blank

#     def __str__(self):
#         return self.user.username

# class ProductCategory(models.Model):
#     title=models.CharField(max_length=200)
#     detail=models.TextField(null=True)

#     def __str__(self):
#         return self.title

# class Product(models.Model):
#     title=models.CharField(max_length=200)
#     detail=models.TextField(null=True)
#     price=models.FloatField()

#     def __str__(self):
#         return self.title



#notes from tutorial


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class Room(models.Model):
    code = models.CharField(
     max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)