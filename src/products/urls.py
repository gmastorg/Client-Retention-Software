from django.urls import path
from .views import (
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

#This is used in products/model.py in the get_absolute_url function
app_name = "products"

urlpatterns = [
    path('create/', product_create_view),
    path("<int:prod_id>/", dynamic_lookup_view, name="product-detail"),
    path("<int:prod_id>/delete/", product_delete_view, name="product-delete"),
    path("", product_list_view, name="product-list"),
    path("<int:prod_id>/update/", product_update_view, name="product-update"),
]