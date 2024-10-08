# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataDompet(models.Model):
    username_dompet = models.ForeignKey('Username', models.DO_NOTHING, db_column='username_dompet')
    saldo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_dompet'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Keranjang(models.Model):
    id_keranjang = models.OneToOneField('Produk', models.DO_NOTHING, db_column='id_keranjang', primary_key=True)
    jumlah = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'keranjang'


class OrderPurchasehistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    total_paid = models.IntegerField()
    is_paid = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, to_field='username')
    product_name_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'order_purchasehistory'


class OrdersHistoryorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    total_paid = models.IntegerField()
    is_paid = models.IntegerField()
    created_at = models.DateTimeField()
    created_by_id = models.CharField(max_length=150)
    product_name_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'orders_historyorder'


class Produk(models.Model):
    nama_barang = models.CharField(max_length=100)
    gambar = models.CharField(max_length=255, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    harga = models.PositiveIntegerField()
    jumlah = models.PositiveIntegerField()
    is_sold = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produk'


class Purchasehistory(models.Model):
    product_name = models.ForeignKey(Produk, models.DO_NOTHING, db_column='product_name')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    total_paid = models.IntegerField(blank=True, null=True)
    is_paid = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchasehistory'


class UserProfile(models.Model):
    username_acc = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='username_acc', to_field='username')
    gambar = models.CharField(max_length=255, blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'


class Username(models.Model):
    username_akun = models.CharField(primary_key=True, max_length=100)
    password_akun = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'username'
