from django import forms


class Form(forms.Form):
    Enter_your_inquiry = forms.CharField(widget=forms.Textarea)
    Your_phone = forms.CharField(max_length=10,min_length=10)
    email = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
