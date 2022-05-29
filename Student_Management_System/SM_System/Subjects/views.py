from django.shortcuts import render, redirect
from Students.models import subjects
from .form import subjectsForm
# Create your views here.
from Students.models import students


def subjects_base(request):
    if request.method == "POST":
        form = subjectsForm(request.POST)
        if form.is_valid():
            form.save()
            all_subjects = subjects.objects.all()
            return render(request, 'show_subjects.html', {'all_subjects': all_subjects})
    else:
        all_subjects = subjects.objects.all()
        all_students = students.objects.all()
        return render(request, 'show_subjects.html', {'all_subjects': all_subjects, 'all_students': all_students})


def delete_subject(request, list_id):
    item = subjects.objects.get(pk=list_id)
    item.delete()
    return redirect('subjects')

def edit_subject(request, list_id):
    if request.method == "POST":
        subject = subjects.objects.get(pk=list_id)
        form = subjectsForm(request.POST or None, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        subject = subjects.objects.get(pk=list_id)
        return render(request, 'edit_subjects.html', {'subject': subject})
