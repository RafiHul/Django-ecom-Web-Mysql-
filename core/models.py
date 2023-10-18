from django.db import models

class Keranjang(models.Model):
    id_keranjang = models.OneToOneField('Produk', models.DO_NOTHING, db_column='id_keranjang', primary_key=True)
    jumlah = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'keranjang'

class Produk(models.Model):
    nama_barang = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to="item_images", null=True, blank=True)
    harga = models.PositiveIntegerField()
    jumlah = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'produk'

    def __str__(self):
        return self.nama_barang

class Username(models.Model):
    username_akun = models.CharField(primary_key=True, max_length=100)
    password_akun = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'username'
