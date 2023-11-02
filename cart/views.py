from django.shortcuts import render,redirect,get_object_or_404
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
def add_cart(request,pk):
    cart = Cart(request)
    produk = get_object_or_404(Produk,pk=pk)
    price = produk.harga
    mm = cart.add(produk_id=pk,price=price)
    if mm:
        messages.success(request, 'Produk berhasil ditambahkan ke keranjang.')
    return redirect('cart:cart_view')

@login_required
def checkout(request,pk):
    cart = Cart(request)
    return render(request, 'cart/checkout.html',{
        'qck': cart,
    })