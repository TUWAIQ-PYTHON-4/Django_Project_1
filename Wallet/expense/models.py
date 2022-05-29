from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category



class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    bill = models.ImageField(upload_to='expense/bill_img', default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering: ['-date']