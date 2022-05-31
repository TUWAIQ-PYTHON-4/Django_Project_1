from django.contrib import admin

from .models import Seller, Product


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    # date_hierarchy = 'date_created'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ['name', 'price']


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
