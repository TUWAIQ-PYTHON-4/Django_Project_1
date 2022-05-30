from django.db import models

class Publisher (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='publisher/photos/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    Publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photos/')
    def __str__(self):
        return self.name