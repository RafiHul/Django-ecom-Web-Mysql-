from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User#user importan di atas
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.lower() in ['vendor','settings','topup','null','admin']:
            raise forms.ValidationError(f"nama pengguna {username} tidak di perbolehkan")
        return username

class TopupSaldo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("saldo",)

    saldo = forms.IntegerField(min_value=0,widget=forms.TextInput(attrs={
        'placeholder': '....',
        'class': 'w-full border p-2 rounded-md'
    }))

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username",)
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter New Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class EditImageForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("gambar",)
        widgets = {
            "gambar":forms.FileInput(attrs={
            'class': 'w-full py-4 px-6 rounded-xl'
            })
        }
