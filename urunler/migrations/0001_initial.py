# Generated by Django 3.2.12 on 2022-08-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('aciklama', models.TextField(max_length=500)),
                ('fiyat', models.IntegerField()),
                ('resim', models.FileField(blank=True, null=True, upload_to='urunler/')),
            ],
        ),
    ]
