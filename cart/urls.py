from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/',views.cart_view,name='cart_view'),
    path('cart/add/<int:pk>',views.add_cart,name='add_cart'),
    path('cart/checkout/<int:pk>',views.checkout,name='checkout'),
]
