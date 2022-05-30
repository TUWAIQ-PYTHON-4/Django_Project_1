from django.db import models
from django.db import models

# Create your models here.

class cloth(models.Model):

    title = models.CharField(max_length=512)
    desc = models.TextField()
    price = models.IntegerField()

    # To represent the model as a string
    def __str__(self) -> str:
        return self.title



class seller(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    profile=models.TextField(blank=True)
    photo=models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return  self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField(blank=True)
    price=models.IntegerField()
    seller=models.ForeignKey(seller,on_delete=models.DO_NOTHING)
    photo=models.ImageField(upload_to='product/photos/')
    def __str__(self):
        return self.name


