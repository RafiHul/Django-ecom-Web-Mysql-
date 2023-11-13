from django.db import models
from django.contrib.auth.models import User

class Keranjang(models.Model):
    id_keranjang = models.OneToOneField('Produk', models.DO_NOTHING, db_column='id_keranjang', primary_key=True)
    jumlah = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'keranjang'

class Produk(models.Model):
    nama_barang = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to="item_images", null=True, blank=True)
    deskripsi = models.TextField(blank=True,null=True)
    harga = models.PositiveIntegerField()
    jumlah = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'produk'

    def __str__(self):
        return self.nama_barang
