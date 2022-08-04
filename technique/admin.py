from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ['name','company','price','abaut','img','condition','color','country','size','features']
    list_filter = ['price']
    search_fields = ["name__icontains"]
    
    def show_buy(self, obj):
        return format_html(f"<a href='ss'>buy</a>")


@admin.register(Aksiya)
class AksiyaAdmin(admin.ModelAdmin):
    list_display = ['name','company','new_price','old_price','abaut','img','condition','color','country','size','features']
    list_filter = ['new_price']
    search_fields = ["name__icontains"]
    
    def show_buy(self, obj):
        return format_html(f"<a href='ss'>buy</a>")


    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'technique']

    fields = ['technique']


