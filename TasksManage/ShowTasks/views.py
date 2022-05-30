from django.shortcuts import render, redirect
from .models import Tasks, TaskOwner
from .forms import TaskModelForm


# Create your views here.
def home(request):
    tasks_items = Tasks.objects.all()

    return render(request, 'home.html', {'tasks_items': tasks_items})


def add(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            new_task = form.save()

    form = TaskModelForm()

    return render(request, "AddPage.html", {"method": request.method, "form": form})


def search(request):
    pass


def delete(request, Tasks_id):
    item = Tasks.objects.get(pk=Tasks_id)
    item.delete()
    return redirect('home')


def edit(request, Tasks_id):
    pass
