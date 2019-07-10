from django.contrib import admin
from .models import Show

# Register your models here.
@admin.register(Show)
#admin.site.register(Show)

#This will show the attributes of the objects in the admin view
class ShowAdmin(admin.ModelAdmin):
    list_display = ['show_name', 'year', 'city', 'state',]