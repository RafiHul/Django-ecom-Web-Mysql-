from django import forms
from core.models import Produk

class QuantityForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ("jumlah",)
        widgets = {
            'jumlah': forms.NumberInput(attrs={
                'id': 'jumlahBeli',
                'type': 'number',
                'min': '0',
            })
        }