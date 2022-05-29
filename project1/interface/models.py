from statistics import mode
from django.db import models
class seller(models.Model):
    name = models.CharField(max_length=200,help_text="Type your name")
    email = models.EmailField(max_length=75,help_text="Type your Email")
    phone = models.CharField(max_length=10,help_text="Type your phone number start with 05")
    date_created = models.DateTimeField(auto_now_add=True,help_text="Date created")
    profile = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    item = models.CharField(max_length=100,help_text="Type name of the item")
    brand = models.CharField(max_length=100,help_text="Type the brand name")
    description = models.TextField(blank=True)
    price = models.IntegerField(help_text="Type price of the product")
    seller = models.ForeignKey(seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photo/')

    def __str__(self):
        return self.item