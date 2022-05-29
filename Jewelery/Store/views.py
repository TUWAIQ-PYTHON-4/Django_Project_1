from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Products


# Create your views here.
def home(request):
    return render(request, 'home.html')


def products(request):
    products = Products.objects.all()
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {'products': paged_products}
    return render(request, 'products.html', context)
