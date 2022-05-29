from django.db import models


# Create your models here.
class Barista(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    type_coffee = models.CharField(max_length=10)  # hot or cold
    photo = models.ImageField(upload_to='Barista/photos/')


    def __str__(self):
        return self.name


class Coffee(models.Model):
    name_coffee = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    price = models.IntegerField()
    barista = models.ForeignKey(Barista, on_delete=models.DO_NOTHING)#Because the barista has more than one type of coffee
    photo = models.ImageField(upload_to='coffee/photos/')

    def __str__(self):
        return self.name_coffee


class Sweet(models.Model):
    name_sweet = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='coffee/photos/')

    def _str_(self):
        return self.name_sweet