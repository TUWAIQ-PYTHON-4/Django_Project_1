from django.db import models


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=200)
    overview = models.TextField()
    photo = models.ImageField(upload_to='brand/photos/')
    website = models.URLField()

    def __str__(self):
        return self.name
