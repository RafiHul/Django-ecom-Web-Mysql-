from django.db import models
from django.contrib.auth.models import User

from core.models import Produk

class Purchasehistory(models.Model):
    product_name = models.ForeignKey(Produk, related_name='produk_name', on_delete=models.CASCADE, db_column='product_name')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    total_paid = models.IntegerField(blank=True)
    is_paid = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'purchasehistory'

    def __str__(self):
        return f"{str(self.created_by)},{str(self.product_name)}"