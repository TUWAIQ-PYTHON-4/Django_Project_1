from django.db import models


# Create your models here.
class Designer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='designer/photo/')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    designer = models.ForeignKey(Designer, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photo/')

    def __str__(self):
        return self.name
