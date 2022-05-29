from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


# Create your views here.
def rev(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


def show(request):
    reviews = Review.objects.all()
    return render(request, 'show.html', {'reviews': reviews})


def edit(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'edit.html', {'review': review})


def update(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'review': review})


def destroy(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/show')
