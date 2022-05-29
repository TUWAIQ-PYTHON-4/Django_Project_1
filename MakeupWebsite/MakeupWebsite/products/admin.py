from django.contrib import admin
from .models import Products, Brand


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    list_filter = ('brand_name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Products, ProductsAdmin)

