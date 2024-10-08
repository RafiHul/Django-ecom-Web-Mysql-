# Generated by Django 4.2.5 on 2023-10-18 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDompet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('saldo', models.IntegerField()),
            ],
            options={
                'db_table': 'data_dompet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=100)),
                ('gambar', models.TextField()),
                ('harga', models.PositiveIntegerField()),
                ('jumlah', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'produk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('username_akun', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password_akun', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'username',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keranjang',
            fields=[
                ('id_keranjang', models.OneToOneField(db_column='id_keranjang', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.produk')),
                ('jumlah', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'keranjang',
                'managed': False,
            },
        ),
    ]
