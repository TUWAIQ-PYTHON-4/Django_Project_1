from django.shortcuts import render, redirect

# Create your views here.
from .form import studentsForm
from .models import students, subjects


def students_base(request):
    if request.method == "POST":
        form = studentsForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_students = students.objects.all()

            return render(request, 'show_students.html', {'all_students': all_students})
    else:
        all_students = students.objects.all()
        return render(request, 'show_students.html', {'all_students': all_students})


def delete(request, list_id):
    item = students.objects.get(pk=list_id)
    item.delete()
    return redirect('students')

def edit(request, list_id):
    if request.method == "POST":
        student = students.objects.get(pk=list_id)
        form = studentsForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        student = students.objects.get(pk=list_id)
        return render(request, 'edit_student.html', {'student': student})

def show_student_subjects(request, list_id):
    if request.method == "POST":
        student = students.objects.get(pk=list_id)
        form = studentsForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        student = students.objects.get(pk=list_id)
        all_subjects = subjects.objects.filter(student_id = list_id )
        return render(request, 'show_student_subjects.html', {'student': student, 'all_subjects': all_subjects})