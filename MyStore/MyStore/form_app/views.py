from django.shortcuts import render
from .form import ExampleForm

def form_app(request):
    form = ExampleForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form-app.html", {"method": request.method, "form": form})
















