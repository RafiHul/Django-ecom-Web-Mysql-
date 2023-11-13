from django.shortcuts import render
from .models import Produk, Keranjang

def index(request):
    produk = Produk.objects.filter(is_sold=False).exclude(jumlah=0)
    return render(request, 'core/index.html', {
        'produk': produk,
    })
