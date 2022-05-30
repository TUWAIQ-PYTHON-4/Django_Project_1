from django import forms
from .models import Tasks


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"

