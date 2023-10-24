from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import SignupForm, TopupSaldo
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            get_username = form.cleaned_data['username']
            user = User.objects.get(username=get_username)
            wall = UserProfile(username_acc=user)
            wall.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'account/signup.html',{
        'form': form
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('core:index')

@login_required
def profile(request):

    profile = UserProfile.objects.get(username_acc=request.user)
    return render(request, 'account/profile.html', {
        'profile': profile,
    })

@login_required
def topup(request):
    if request.method == 'POST':
        form = TopupSaldo(request.POST)
        if form.is_valid():
            saldo = form.cleaned_data['saldo']
            
            # Periksa apakah saldo positif
            if saldo > 0:
                # Ambil objek UserProfile yang sesuai dengan user saat ini
                user_profile = UserProfile.objects.get(username_acc=request.user)
                
                # Perbarui saldo pada objek UserProfile
                user_profile.saldo += saldo
                user_profile.save()
                
                # Redirect ke halaman profil
                return redirect('account:profile')
            else:
                messages.error(request, "Masukkan angka yang benar")
        else:
            messages.error(request, "Form tidak valid. Pastikan Anda memasukkan angka yang benar.")
    else:
        form = TopupSaldo()
    
    formsd = UserProfile.objects.get(username_acc=request.user)
    return render(request, 'account/topup.html', {
        'form': formsd.saldo,
        'form1': form,
    })

