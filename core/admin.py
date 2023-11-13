from django.contrib import admin
from .models import Produk, Keranjang
from account.models import UserProfile
# Register your models here.

admin.site.register(Produk)
admin.site.register(Keranjang)
admin.site.register(UserProfile)