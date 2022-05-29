from django.contrib import admin
from .models import Expense, Category
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'category', 'date', 'bill',)
    list_filter = ('amount', 'category', 'date')
    search_fields = ('category',)
    empty_value_display = '-empty-'

    list_per_page = 5


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)