from django import forms
from .models import Reviews


class revForm(forms.Form):
    text_input = forms.CharField(max_length=20)
    text_area = forms.CharField(widget=forms.Textarea)



class reviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'name',
            'reviews_description',
        ]