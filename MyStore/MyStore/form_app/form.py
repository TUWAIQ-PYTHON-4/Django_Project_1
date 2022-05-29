from django import forms
RADIO_CHOICES = (("Value One", "Abha"),("Value Two", "Riyadh"),
                 ("Value Three", "Dammam"))

MOVIE_CHOICES = (
("AM", (("1", " 10 AM"), ("2", "8 AM"))),
("PM", (("3", "8 PM"),("4", "10 PM")))
)


class ExampleForm(forms.Form):
    Name = forms.CharField(max_length=3)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    test = forms.BooleanField()
    Chooseـtheـcity = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    Delivery_time = forms.ChoiceField(choices=MOVIE_CHOICES)
    Delivery_time = forms.MultipleChoiceField(required=False, choices=MOVIE_CHOICES)
    Notes = forms.CharField(widget=forms.Textarea)

    Nuber_of_Products = forms.IntegerField(min_value=1, max_value=50)
    Serial_Products = forms.DecimalField(max_digits=5, decimal_places=3)

    email_input = forms.EmailField()
    Delivery_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")