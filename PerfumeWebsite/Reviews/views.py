from django.shortcuts import render, redirect
from .forms import RevForm
from django.http import HttpResponseRedirect ,HttpRequest
from .models import Reviews


def reviews_f(request):
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
    return redirect('reviews/reviews.html')