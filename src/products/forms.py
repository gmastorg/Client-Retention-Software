from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price',
                'size',
                'active'
                ]

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    size = forms.CharField()
    active = forms.BooleanField()