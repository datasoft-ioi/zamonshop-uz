# Generated by Django 3.2.13 on 2023-05-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_top_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='top_image',
            field=models.ImageField(blank=True, null=True, upload_to='cat_img/%Y/%m/%d'),
        ),
    ]
