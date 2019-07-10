from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sector
from .forms import SectorForm
from django.urls import reverse

#To use Class Based Views, import theses
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

#These are Class Based Views

#Allows the user to view a list of Show objects
class SectorListView(ListView):
    template_name = "sectors/sector_list.html/"
    queryset = Sector.objects.all()

#Allows the user to view the details of a selected Show object
class SectorDetailView(DetailView):
    template_name = "sectors/sector_detail.html/"
    queryset = Sector.objects.all()
    #You do not have to have a query set here, however you can use it to limit which items
    #are available in the queryset by filtering the objects in the set

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Sector, id=id)

#Allows the user to create a new Show object
class SectorCreateView(CreateView):
    template_name = "sectors/sector_create.html/"
    form_class = SectorForm
    queryset = Sector.objects.all()
    #To override the get_absolute_url from shows/model.py use the line below
    #success_url = "/shows/"

#Allows the user to update/change an existing Show object
class SectorUpdateView(UpdateView):
    template_name = "sectors/sector_create.html/"
    form_class = SectorForm
    queryset = Sector.objects.all()


    #Method that returns the object corresonding to an id
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Sector, id=id)


#Allows the user to delete an existing Show object
class SectorDeleteView(DeleteView):
    template_name = "sectors/sector_delete.html/"
    queryset = Sector.objects.all()
    
    #Must have success_url for DeleteView bc the default is show_detail.html but the object no longer exists
    def get_success_url(self):
        return reverse('sectors:sector-list')


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Sector, id=id)