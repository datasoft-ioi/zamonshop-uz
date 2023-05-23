# Generated by Django 3.2.13 on 2023-05-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='banner/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SwipperBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='bnr_swiper/%Y/%m/%d')),
            ],
        ),
    ]
