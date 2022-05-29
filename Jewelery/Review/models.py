from django.db import models


# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=20)
    review = models.TextField(max_length=100)

    def __str__(self):
        return "%s"%(self.name)

    class Mate:
        db_table = "Review"
