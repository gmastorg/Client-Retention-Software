from django.urls import path
from .views import (
    ClientView,
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
)

app_name = "clients"

urlpatterns = [
    #if you specify a template_name HERE vvvvvvvvvvvvvvv it will override template_name in you class see clients/views
    path('', ClientListView.as_view(template_name = "clients/client_list.html"), name="client-list"),
    path('about/', ClientView.as_view( template_name = "clients/about_clients.html"), name="client-about"),
    path("<int:id>/", ClientView.as_view(), name="client-detail"),
    path("<int:id>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("create/", ClientCreateView.as_view(), name="client-create"),
    path("<int:id>/update/", ClientUpdateView.as_view(), name="client-update"),
]