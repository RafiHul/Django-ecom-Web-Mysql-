from django import forms
from .models import Purchasehistory

CLASS_INPUT = "w-full p-5 rounded-xl"

class Purchaseform(forms.ModelForm):
    class Meta:
        model = Purchasehistory
        fields = ("first_name","last_name","address","zipcode","city")
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "w-full p-5 rounded-xl"
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
        }
