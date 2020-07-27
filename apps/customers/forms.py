from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'customer_address', 'customer_district', 'reference_address', 'customer_phone']

        def __init__(self, attrs=None):
            widget = {
            'first_name': forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'uk-input'}),
            'customer_address': forms.TextInput(attrs={'class': 'uk-input'}),
            'customer_district': forms.TextInput(attrs={'class': 'uk-input'}),
            'reference_address': forms.TextInput(attrs={'class': 'uk-input'}),
            'customer_phone': forms.TextInput(attrs={'class': 'uk-input'}),
            }
