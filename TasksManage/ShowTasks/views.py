from django.shortcuts import render, redirect
from .models import Tasks, TaskOwner
from .forms import TaskModelForm


# Create your views here.
def home(request):
    if request.GET: # search tasks by title
        search_item = request.GET
        search_item = search_item['search']
        tasks_items = Tasks.objects.filter(title__contains=search_item)

    else: # show all tasks if the search fields is empty
        tasks_items = Tasks.objects.all()

    return render(request, 'home.html', {'tasks_items': tasks_items})


def add(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            tasks_items = form.save()

    form = TaskModelForm()

    return render(request, 'AddPage.html', {"method": request.method, "form": form})


def delete(request, Tasks_id):
    item = Tasks.objects.get(pk=Tasks_id)
    item.delete()
    return redirect('home')


def edit(request):
    pass
