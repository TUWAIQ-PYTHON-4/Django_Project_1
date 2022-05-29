from django.shortcuts import render, redirect
from .models import Reviews
from .forms import reviewsForm , revForm
def reviews(request):
    if request.method == "POST":
        form = reviewsForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = Reviews.objects.all()
            return render(request, 'reviews/reviews.html', {'all_items': all_items})
    else:
        all_items = Reviews.objects.all()
        return render(request, 'reviews/reviews.html', {'all_items': all_items})
def delete(request, reviews_id):
    item = Reviews.objects.get(pk=reviews_id)
    item.delete()
    return redirect('reviews/reviews.html')
def fexample(request):
    if request.method == "POST":
        form =revForm(request.POST)
    else:
        form =revForm()
    if request.method == "POST":
        form =revForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))
    return render(request, "reviews/reviews.html", {"method": request.method, "form": form})