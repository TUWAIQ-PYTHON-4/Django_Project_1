from django.shortcuts import render, redirect
from .forms import RevForm
from django.http import HttpResponseRedirect ,HttpRequest
from .models import Reviews




'''def reviews_f(request):
    form = RevForm(request.POST or None)
    if request.method == "POST":
        form = RevForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, "reviews/reviews.html", {"form": form})
    else:
       form= RevForm
    return render(request, "reviews/reviews.html", {"form": form})

def reviews_list(request):
    rev_list=Reviews.objects.all()
    context = {'rev_list':rev_list}
    return render(request,"reviews/reviews.html",context)

def delete(request, reviews_id):
    item = Reviews.objects.get(pk=reviews_id)
    item.delete()
    return redirect('reviews/reviews.html')'''

from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Reviews
from .forms import RevForm


def index(request: HttpRequest):
    rev_list = Reviews.objects.all()

    context = {"reviews": rev_list, "display": True}
    response = render(request, 'reviews/reviews.html', context)
    return response


def add_rev(request: HttpRequest):
    if request.method == 'POST':
        revModelForm = RevForm(request.POST, request.FILES)

        if revModelForm.is_valid():
            rev = revModelForm.save()
            return redirect(resolve_url("reviews:index"))

    form = RevForm()
    return render(request, 'reviews/reviews.html', {"form": form})


def list_revs(request: HttpRequest ):
    if request.GET:
        print(request.GET)
    rev_list = []
    context = {"rev_list": rev_list[int()]}
    return render(request, 'reviews/reviews.html', context)

def delete(request, reviews_id):
    item = Reviews.objects.get(pk=reviews_id)
    item.delete()
    return redirect('reviews/reviews.html')


def edit(request, reviews_id):
    if request.method == "POST":
        item = Reviews.objects.get(pk=reviews_id)
        form = RevForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('reviews/reviews.html')
    else:
        item = Reviews.objects.get(pk=reviews_id)
        return render(request, 'edit.html', {'item': item})