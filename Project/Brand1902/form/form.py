from django import forms
from .models import Form




class FormForm(forms.Form):
    class Meta:
        model = Form
        fields = '__all__'