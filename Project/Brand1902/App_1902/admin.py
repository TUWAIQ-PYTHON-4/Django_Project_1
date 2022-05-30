from django.contrib import admin
from .models import seller, Product

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone')
    date_hierarchy = 'date_created'

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('item', 'brand', 'price','seller')
    list_filter = ('brand','seller')
    search_fields = ['title','price']


admin.site.register(seller,SellerAdmin)
admin.site.register(Product,ProductsAdmin)