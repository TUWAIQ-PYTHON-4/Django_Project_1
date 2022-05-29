from django.shortcuts import render
from .models import Coffee,Sweet ##name from model

def home(reguest):
    return render(reguest,'home.html')

def menu(reguest):

    menus=Coffee.objects.all()
    context={'menu':menus}
    return render(reguest,'menu.html',context)


def sweet(reguest):

    sweets=Sweet.objects.all()
    context={'sweet':sweets}
    return render(reguest,'sweet.html',context)