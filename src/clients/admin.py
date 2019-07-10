from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)

#This will show the attributes of the objects in the admin view
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_city', 'client_state',]