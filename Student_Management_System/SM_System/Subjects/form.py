from django import forms
from Students.models import subjects

class subjectsForm(forms.ModelForm):
    class Meta:
        model = subjects
        fields = '__all__'