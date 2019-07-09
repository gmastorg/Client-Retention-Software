from django.urls import path
from .views import (
    ShowListView,
    ShowDetailView,
    ShowCreateView,
    ShowUpdateView,
    ShowDeleteView
    )

#This is called namespace
app_name = "shows"

urlpatterns = [
    path('create/', ShowCreateView.as_view(), name="show-create"),
    path("<int:id>/", ShowDetailView.as_view(), name="show-detail"), #can use int:pk instead of int:id
    path("<int:id>/delete/", ShowDeleteView.as_view(), name="show-delete"),
    path("", ShowListView.as_view(), name="show-list"), #Class-based view - see shows/views.py
    #By default, django looks for url named app/modelname_list or shows/show_list.html
    path("<int:id>/update/", ShowUpdateView.as_view(), name="show-update"),
]