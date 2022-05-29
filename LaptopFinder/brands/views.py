from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Brand
from .forms import BrandForm


# Create your views here.
def add_brand(request: HttpRequest):
    submitted = False
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_brand?submitted=True')
    else:
        form = BrandForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_brand.html', {'form': form, 'submitted': submitted})


def brand_list(request: HttpRequest):
    brands_list = Brand.objects.all()
    context = {
        'brands_list': brands_list,
    }
    return render(request, 'brands.html', context)


def show_brand(request: HttpRequest, brand_id: int):
    brand = Brand.objects.get(pk=brand_id)
    return render(request, 'show_brand.html', {'brand': brand})
