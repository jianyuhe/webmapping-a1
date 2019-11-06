from django.contrib.gis.admin import OSMGeoAdmin
from address.models import shop
from django.contrib import admin


@admin.register(shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'type', 'location')
