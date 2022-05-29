from django.contrib import admin
from .models import Products, Designer


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'website')
    list_filter = ('phone',)
    search_fields = ('name',)


admin.site.register(Products)
admin.site.register(Designer,ProductsAdmin)
