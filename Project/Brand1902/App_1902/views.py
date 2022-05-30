from django.shortcuts import render
from .models import seller, Product

def base(request):
    return render(request,'base.html')
def home(request):
    sell = seller.objects.all()
    context = {'sell': sell}
    return render(request,'home.html',context)
def Product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)
