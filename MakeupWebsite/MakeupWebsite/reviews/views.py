from django.shortcuts import render, redirect
from .models import Reviews
from .forms import revForm
from . import models


def review(request):

    if request.method == "POST":
        form = revForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = models.Reviews.objects.all()
            return render(request, 'reviews/reviews.html', {"method":request.method,'all_items': all_items})
    else:
        all_items = Reviews.objects.all()
        return render(request, 'reviews/reviews.html', {"method":request.method,'all_items': all_items})


def delete(request, Reviews_id):
    item = Reviews.objects.get(pk=Reviews_id)
    item.delete()
    return redirect('reviews/reviews.html')

