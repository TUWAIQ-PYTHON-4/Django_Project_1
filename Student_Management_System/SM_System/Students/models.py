from django.db import models


class students(models.Model):
    studentName = models.CharField(max_length=50 )
    studentId = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.studentName

class subjects(models.Model):
    subjectName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/photos/')
    student = models.ForeignKey(students, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.subjectName