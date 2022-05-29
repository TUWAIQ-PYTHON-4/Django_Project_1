from django.contrib import admin
from .models import Barista, Coffee ,Sweet


# Register your models here.
class coffee(admin.ModelAdmin):
    list_display = ('name_coffee', 'discription', 'price',)
    list_filter = ('name_coffee',)


admin.site.register(Coffee, coffee)
admin.site.register(Barista)
admin.site.register(Sweet)