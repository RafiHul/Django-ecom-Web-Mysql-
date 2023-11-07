from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import Produk
from .cart import Cart

@login_required
def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html',{
        'cart': cart
    })

@login_required
def add_pk(request,pk,price,quantity):
    request.session['selected_product'] = {"pk":pk,'price':price,'quantity':quantity,'total':int(price) * int(quantity)}
    return redirect('cart:checkout')

@login_required
def checkout_view(request):
    selected_product = request.session.get('selected_product')

    if selected_product:
        pk = selected_product.get('pk')
        price = selected_product.get('price')
        quantity = selected_product.get('quantity')
        total = selected_product.get('total')
        
        messages.success(request, 'Produk berhasil ditambahkan ke keranjang.')
    return render(request, 'cart/checkout.html',{
        'price': price,
        'total': total,
        'quantity':quantity,
    })

@login_required
def checkout(request,pk):
    produk = Produk.objects.get(pk=pk)
    return render(request, 'cart/checkout.html',{
        'qck': produk,
    })