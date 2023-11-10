from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/',views.cart_view,name='cart_view'),
    path('cart/checkout/',views.checkout_view,name='checkout'),
    path('cart/confirmcheckout/',views.checkout,name='confirmcheckout'),
    path('cart/checkout/<int:pk>/<int:price>/',views.add_pk,name='add_checkout')
]
