from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)

#This will show the attributes of the objects in the admin view
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',]
