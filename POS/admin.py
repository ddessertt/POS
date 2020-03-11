from django.contrib import admin
from POS.models import Type, Product
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Type, TypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    list_per_page = 10
    list_filter = ['name', 'price']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)