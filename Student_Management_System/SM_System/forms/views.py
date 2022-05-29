from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .form import Form



def formsapp(request):
    if request.method == "POST":
        form = Form(request.POST)
    else:
        form = Form()
    if request.method == "POST":
        form = Form(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form_app.html", {"method": request.method, 'form': form})

