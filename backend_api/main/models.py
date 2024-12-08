from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) # CASCADE allows to delete all the data of the user when deleting the user
    address = models.TextField(null=True) # user can leave the field in blank

    def __str__(self):
        return self.user.username

class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()

    def __str__(self):
        return self.title
