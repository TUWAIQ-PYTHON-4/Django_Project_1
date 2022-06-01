from typing_extensions import Required
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category



class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField(null=True)
    bill = models.ImageField(upload_to='expense/bill_img', blank=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        ordering: ['-date']
