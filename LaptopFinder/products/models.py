from django.db import models

Type_Choices = (
    ("Power User", "Power User"),
    ("Everyday use", "Everyday use"),
    ("Creative professional", "Creative professional"),
    ("Business", "Business"),
    ("Gaming", "Gaming"),
)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    type = models.CharField(max_length=500, choices=Type_Choices)
    photo = models.ImageField(blank=True, upload_to='product/photos/')
    brand_name = models.ForeignKey('brands.Brand', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name + ' ' + self.description + ' ' + str(self.price) + ' ' + self.type + \
               str(self.photo) + ' ' + str(self.brand_name)
