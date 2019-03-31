# Generated by Django 2.1.7 on 2019-03-30 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partai', '0001_initial'),
        ('dapil', '0001_initial'),
        ('kategori', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caleg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nomor_urut', models.IntegerField()),
                ('isprtai', models.BooleanField(default=False)),
                ('dapil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calegs', to='dapil.Dapil')),
                ('kategoricaleg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kategori.KategoriCaleg')),
                ('partai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partai.Partai')),
            ],
        ),
    ]
