from django.contrib import admin
from .models import Tasks, TaskOwner


class TasksAdmin(admin.ModelAdmin):  # Customize the Admin page using list_filter
    list_display = ('title', 'description', 'created_date')


class TasksOwnerAdmin(admin.ModelAdmin):  # Customize the Admin page using list_display
    list_filter = ('name',)


# Register your models on the Admin page.
admin.site.register(Tasks, TasksAdmin)
admin.site.register(TaskOwner, TasksOwnerAdmin)
