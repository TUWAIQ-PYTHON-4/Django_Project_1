from django.shortcuts import render
from .models import Product
# from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'products/home.html')


def products(request):
    product = products.objects.all()
    context ={'product': products}
    return render(request,'products/products.html',context)




