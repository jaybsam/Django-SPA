# -*- coding: utf-8 -*-
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'uk-input col-md-6 uk-margin-small-bottom'
        }
        self.fields['description'].widget.attrs = {
            'class': 'uk-input col-md-6 uk-margin-small-bottom'
        }
        self.fields['price'].widget.attrs = {
            'class': 'uk-input col-md-6 uk-margin-small-bottom',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Product
        fields = ('name', 'description', 'price')