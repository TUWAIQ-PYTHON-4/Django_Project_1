from django import forms
from .models import Products

RADIO_CHOICES = (
    ("Value One", "Good"), ("Value Two", "Average"), ("Value Three", "Bad")
)


class FeedbackForm(forms.Form):
    chose_one = forms.ChoiceField(choices=RADIO_CHOICES)
    Feedback = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")


class ListForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
