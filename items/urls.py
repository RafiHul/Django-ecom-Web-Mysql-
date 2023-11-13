from django.urls import path, include
from . import views

app_name = "items"

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('new/',views.new,name='new'),
]
