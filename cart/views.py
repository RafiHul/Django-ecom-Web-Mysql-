from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import Produk
from account.models import UserProfile
from .forms import Purchaseform
from .cart import Cart
from .models import Purchasehistory

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
    total = selected_product.get('total')
    quantity = selected_product.get('quantity')
    pk = selected_product.get('pk')
    if request.method == 'POST':
        form = Purchaseform(request.POST)
        if selected_product:
            if form.is_valid():
                print(total,pk,quantity)
                form.save()
                return redirect('cart:confirmcheckout')
    else:
        form = Purchaseform(initial={'quantity':quantity,'total_paid':total,"product_name":pk})
        
    return render(request, 'cart/checkout.html',{
        'total': total,
        'dompet': dompet,
        'form': form,
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

@login_required
def history(request):
    history = Purchasehistory.objects.filter(created_by=request.user)
    return render(request, 'history/history.html',{
        'history':history,
    })
        
