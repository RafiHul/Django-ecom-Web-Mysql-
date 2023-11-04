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
def add_pk(request,pk,price):
    request.session['selected_product'] = {"pk":pk,'price':price}
    return redirect('cart:checkout')

@login_required
def add_checkout(request):
    selected_product = request.session.get('selected_product')

    if selected_product:
        pk = selected_product.get('pk')
        price = selected_product.get('price')

        cart = Cart(request)
        cart.add(produk_id=pk,price=price)
        
        messages.success(request, 'Produk berhasil ditambahkan ke keranjang.')
    return render(request, 'cart/checkout.html',{
        'cart': cart,
    })

@login_required
def checkout(request,pk):
    produk = Produk.objects.get(pk=pk)
    return render(request, 'cart/checkout.html',{
        'qck': produk,
    })