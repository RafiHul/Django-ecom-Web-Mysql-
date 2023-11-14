from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rafih/admoon/defender/',include('defender.urls')),
    path('rafih/admoon/', admin.site.urls),
    path('',include('core.urls')),
    path('',include('account.urls')),
    path('',include('cart.urls')),
    path('items/',include("items.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
