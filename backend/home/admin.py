from django.contrib import admin

from .models import Banner, SwipperBanner, TwoTanla

from mptt.admin import DraggableMPTTAdmin


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

@admin.register(SwipperBanner)
class SwipperBannerAdmin(admin.ModelAdmin):
    pass

@admin.register(TwoTanla)
class TwoTanlaBannerAdmin(admin.ModelAdmin):
    pass





