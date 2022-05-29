from django.contrib import admin
from .models import Brand


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'overview', 'photo', 'website')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
