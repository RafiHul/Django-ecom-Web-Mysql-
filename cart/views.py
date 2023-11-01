from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


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
    mm = cart.add(produk_id=pk)
    if mm:
        messages.success(request, 'Produk berhasil ditambahkan ke keranjang.')
    return redirect('cart:cart_view')

@login_required
def checkout(request,pk):
    cart = Cart(request)
    return render(request, 'cart/checkout.html',{
        'cart':cart,
    })