from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .models import Products
from .forms import FeedbackForm, ListForm


def home(request):
    home = Products.objects.all()
    context = {'home': home}
    return render(request, 'home.html', context)


def add_products(request: HttpRequest):
    if request.method == 'POST':
        listForm = ListForm(request.POST, request.FILES)

        if listForm.is_valid():
            products = listForm.save()
            return redirect(resolve_url("home"))

    form = ListForm()
    return render(request, 'add_products.html', {"form": form})


def feedback(request):
    return render(request, 'feedback.html')


def form_feedback(request):
    form = FeedbackForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "feedback.html", {"method": request.method, "form": form})


def delete(request, Products_id):
    name = Products.objects.get(pk=Products_id)
    name.delete()
    return redirect('home')


def edit(request, Products_id):
    if request.method == "POST":
        name = Products.objects.get(pk=Products_id)
        form = ListForm(request.POST or None, instance=name)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        name = Products.objects.get(pk=Products_id)
        return render(request, 'edit.html', {'name': name})
