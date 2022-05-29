from django.contrib import admin
from .models import students, subjects

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('studentName', 'studentId', 'email' , 'phone')



class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('subjectName', 'description', 'code')
    list_filter = ('student',)




admin.site.register(students , StudentsAdmin)
admin.site.register(subjects ,SubjectsAdmin)



