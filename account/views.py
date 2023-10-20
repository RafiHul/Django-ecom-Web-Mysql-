from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'account/signup.html',{
        'form': form
    })

@login_required
def profile(request,user):
    userss = get_object_or_404(UserProfile, username_acc=user)

    return render(request, 'account\profile.html',{
        'profile':profile,
    })
