from django import forms
from .models import Reviews


class revForm(forms.Form):
    text_input = forms.CharField(max_length=20)
    test_area = forms.CharField()


class reviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
