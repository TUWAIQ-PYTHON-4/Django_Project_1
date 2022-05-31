from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='seller/photo/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING) #ONE TO MANY
    photo = models.ImageField(upload_to='products/photo/')


    def __str__(self):                      # representation on model.
         return self.name


