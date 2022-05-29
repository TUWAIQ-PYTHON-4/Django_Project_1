
from django.db import models
from django.contrib import auth


# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, help_text="The name of the Brand")
    brand_description = models.TextField(help_text="brand's description")

    def __str__(self):
        return self.brand_name


class Products(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the product")
    price = models.IntegerField(help_text="The product's price")
    description = models.TextField(help_text="product's description")
    add_time = models.DateTimeField(auto_now_add=True, help_text="the date & time of adding the product")
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/photos/')

    def __str__(self):
        return self.name


