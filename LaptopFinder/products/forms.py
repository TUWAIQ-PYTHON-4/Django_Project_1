from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ('product_name', 'description', 'price', 'type', 'photo', 'brand_name')
        labels = {
            'product_name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'type': 'Product Type',
            'photo': 'Product Photo',
            'brand_name': 'Brand Name',
        }

