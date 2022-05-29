from django.contrib import admin
from .models import Product,Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name')

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('seller',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Seller)





