from django.db import models


# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(blank=True,upload_to='products/photos/')
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' | ' + str(self.Available)
