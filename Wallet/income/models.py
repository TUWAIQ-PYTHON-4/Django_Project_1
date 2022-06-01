from django.db import models
from django.utils.timezone import now

# Create your models here.



class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Income(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.source

    class Meta:
        ordering: ['-date']