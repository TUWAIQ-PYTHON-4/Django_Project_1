from django import forms
from .models import Form
#
# class comment(forms.ModelForm):
#     class  Meta:
#         model = Form
#         fields = "__all__"


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'