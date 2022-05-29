from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'products/home.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)


