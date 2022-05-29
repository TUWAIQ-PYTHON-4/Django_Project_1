from django.shortcuts import render, redirect
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
import datetime


def index(request):
    categories = Category.objects.all()
    expense = Expense.objects.all()
    paginator = Paginator(expense, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'expense': expense,
        'page_obj': page_obj,
    }
    return render(request, 'expense/index.html', context)


def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expense/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expense/add_expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category=Category.objects.get(category=request.POST['category'])
        bill = request.POST['bill']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expense/add_expense.html', context)

        Expense.objects.create(amount=amount, date=date, category=category, description=description, bill=bill)
        messages.success(request, 'Expense saved successfully')

        return redirect('expense')


def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'expense/edit_expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expense/edit_expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category=Category.objects.get(category=request.POST['category'])
        bill = request.POST['bill']


        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expense/edit_expense.html', context)

        expense.amount = amount
        expense.date = date
        category = Category.objects.get(category=request.POST['category'])
        expense.description = description
        expense.bill = bill

        expense.save()
        messages.success(request, 'Expense updated successfully')

        return redirect('expense')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect('expense')


