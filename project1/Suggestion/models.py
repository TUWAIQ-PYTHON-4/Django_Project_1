from operator import mod
from random import choices
from unicodedata import name
from django.db import models



class Form(models.Model):

    CHOICES = (
        ('Very Important', 'Very Important'),
        ('Important', 'Important'),
        ('General', 'General'),
        ('Not Important', 'Not Important'),
    )

    name = models.CharField(max_length=150,help_text="Type your full name")
    email = models.EmailField(max_length=200,help_text="Type your Email")
    subject = models.CharField(max_length=50)
    importance = models.CharField(max_length=250,choices = CHOICES)
    desc = models.TextField()
    def __str__(self) :
        return self.name