from django.shortcuts import render, redirect
from .models import User
from .forms1 import UserForm


def userList(request):
    users = User.objects.all()
    return render(request, "user-list.html", {'users': users})


def userCreate(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('user-list')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'user-create.html', {'form': form})


def userUpdate(request, id):
    user = User.objects.get(id=id)
    form = UserForm(initial={'title': user.title, 'description': user.description, 'Name': user.author, 'year': user.year})
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/user-list')
            except Exception as e:
                pass
    return render(request, 'user-update.html', {'form': form})


def userDelete(request, id):
    user = User.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('user-list')
