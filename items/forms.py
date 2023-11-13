from django import forms
from core.models import Produk

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItem(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ('nama_barang','gambar','deskripsi','harga','jumlah')
        widgets = {
            'nama_barang': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gambar': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'harga': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'harga': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditItem(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ('nama_barang','gambar','deskripsi','harga','jumlah','is_sold')
        widgets = {
            'nama_barang': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gambar': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'harga': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'harga': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }