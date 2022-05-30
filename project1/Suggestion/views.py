from django.shortcuts import redirect, render
from .forms import FormForm
from .models import Form



def add(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            add = FormForm(request.POST)
            add.save() 
            return redirect('form') 

    form = FormForm()
    return render(request,'add.html',{"form" : form})



def home(request):
    if request.method == "POST":
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
    context = Form.objects.all()
    return render(request,"form.html",{"context":context})


def delete(request, name_id):
    name = Form.objects.get(id=name_id)
    name.delete()
    return redirect('form')

def edit(request, name_id):
    if request.method == "POST":
        item = Form.objects.get(id=name_id)
        form = FormForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        item = Form.objects.get(id=name_id) 
    return render(request,"edit.html",{'item': item})