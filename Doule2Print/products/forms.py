# products/forms.py

from django import forms
from .models import Product, Variety

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description']

class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = ['name', 'image', 'description', 'stock',  'retail_price','wholesale_price']


'''class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['is_wholesale']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['variety', 'quantity']
        widgets = {
            'variety': forms.HiddenInput(),
        }
'''
