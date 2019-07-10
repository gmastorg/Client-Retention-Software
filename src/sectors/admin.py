from django.contrib import admin

from .models import Sector
# Register your models here.
@admin.register(Sector)

#This will show the attributes of the objects in the admin view
class SectorAdmin(admin.ModelAdmin):
    list_display = ['sector_name',]