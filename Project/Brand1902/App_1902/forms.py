from django import forms
from django import forms
from .models import Product

class brand(forms.Form):
    name=forms.CharField(label='Name_pro',max_length=200)
    desc = forms.CharField(label="Movie Desc", widget=forms.widgets.Textarea)
    price=forms.IntegerField()
    #photo=forms.ImageField(upload_to='')


class MovieModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
