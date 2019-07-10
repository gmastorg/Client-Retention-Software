from django.urls import path
from .views import (
    SectorListView,
    SectorDetailView,
    SectorCreateView,
    SectorUpdateView,
    SectorDeleteView
    )

#This is called namespace
app_name = "sectors"

urlpatterns = [
    path('create/', SectorCreateView.as_view(), name="sector-create"),
    path("<int:id>/", SectorDetailView.as_view(), name="sector-detail"), #can use int:pk instead of int:id
    path("<int:id>/delete/", SectorDeleteView.as_view(), name="sector-delete"),
    path("", SectorListView.as_view(), name="sector-list"),
    #By default, django looks for url named app/modelname_list.html
    path("<int:id>/update/", SectorUpdateView.as_view(), name="sector-update"),
]