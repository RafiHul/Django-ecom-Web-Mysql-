from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import Produk
from account.models import UserProfile
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
    dompet = UserProfile.objects.get(username_acc = request.user)
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
        'quantity': quantity,
        'dompet': dompet,
    })

@login_required
def checkout(request):
    selected_product = request.session.get('selected_product')
    dompet = UserProfile.objects.get(username_acc = request.user)
    total = selected_product.get('total')
    pk = selected_product.get('pk')
    quantity = selected_product.get('quantity')
    product = Produk.objects.get(pk=pk)

    if selected_product:
        if dompet.saldo >= total and quantity <= product.jumlah:
            dompet.saldo -= int(total)
            product.jumlah -= int(quantity)
            product.save()
            dompet.save()
            return redirect('account:profile')
        
