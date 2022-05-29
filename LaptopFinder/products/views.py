from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from .forms import ProductForm
from .models import Product


# Create your views here.

def home(request: HttpRequest):
    product_list = Product.objects.all()
    p = Paginator(Product.objects.all(), 3)
    page = request.GET.get('page')
    products = p.get_page(page)
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Product.objects.all()
            return render(request, 'home.html', {'all_items': all_items, 'products': products})
    else:
        all_items = Product.objects.all()
        return render(request, 'home.html', {'all_items': all_items, 'products': products})


def add_product(request: HttpRequest):
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_product?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_product.html', {'form': form, 'submitted': submitted})

def delete_product(request: HttpRequest, id: int):
    item = Product.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect('/')


def update_product(request: HttpRequest, id: int):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update_product.html', {'product': product, 'form': form})


def search_product(request: HttpRequest):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(product_name__icontains=searched) | \
                  Product.objects.filter(type__icontains=searched)
        return render(request, 'search.html', {'searched': searched, 'product': product})
    else:
        return render(request, 'search.html', {})
