from django.db import models


# Create your models here.

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    reviews_description = models.TextField()
    reviews_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
