from django import forms
from .models import Purchasehistory

CLASS_INPUT = "w-full p-5 rounded-xl"

class Purchaseform(forms.ModelForm):
    
    class Meta:
        model = Purchasehistory
        fields = ("first_name","last_name","address","zipcode","city","quantity","total_paid","product_name")
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": CLASS_INPUT
            }),
            "last_name": forms.TextInput(attrs={
                "class": CLASS_INPUT
            }),
            "address": forms.TextInput(attrs={
                "class": CLASS_INPUT
            }),
            "zipcode": forms.TextInput(attrs={
                "class": CLASS_INPUT
            }),
            "city": forms.TextInput(attrs={
                "class": CLASS_INPUT
            }),
            "quantity":forms.TextInput(),
            "total_paid":forms.TextInput(),
            "product_name":forms.TextInput()
        }
