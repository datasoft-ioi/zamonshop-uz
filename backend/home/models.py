from django.db import models

from products.models import Category


class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nomi")
    image = models.ImageField(upload_to="banner/%Y/%m/%d", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title


class SwipperBanner(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nomi")
    image = models.ImageField(upload_to="bnr_swiper/%Y/%m/%d", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    

class TwoTanla(models.Model):
    category = models.ForeignKey(Category, verbose_name="2 Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name
    
    
    