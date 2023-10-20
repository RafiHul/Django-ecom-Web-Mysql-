from django.shortcuts import render
from .models import Produk, Keranjang

def index(request):
    produk = Produk.objects.all()
    return render(request, 'core/index.html', {
        'produk': produk,
    })
