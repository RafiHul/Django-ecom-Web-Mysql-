from django.urls import path
from .forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html',authentication_form=LoginForm), name='login'),
    path('<str:user>/',views.profile,name='profile'),
]
