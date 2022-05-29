from django.contrib import admin
from .models import Products, Seller


class ProductsAdmin(admin.ModelAdmin):
    list_filter = ('seller',)


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profile')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Seller, SellerAdmin)
