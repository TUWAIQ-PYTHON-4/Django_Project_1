from django import forms
from .models import Tasks


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
        labels = {
            "title": "Title of the task",
            "description": "Description of the task",
            "created_date": "Date of the created task",
            "name": "The name of the task owner"
        }


