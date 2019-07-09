from django.shortcuts import render, get_object_or_404, redirect
from .models import Show
from .forms import ShowsForm
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
class ShowListView(ListView):
    template_name = "shows/show_list.html/"
    queryset = Show.objects.all()

#Allows the user to view the details of a selected Show object
class ShowDetailView(DetailView):
    template_name = "shows/show_detail.html/"
    queryset = Show.objects.all()
    #You do not have to have a query set here, however you can use it to limit which items
    #are available in the queryset by filtering the objects in the set

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Show, id=id)

#Allows the user to create a new Show object
class ShowCreateView(CreateView):
    template_name = "shows/show_create.html/"
    form_class = ShowsForm
    queryset = Show.objects.all()
    #To override the get_absolute_url from shows/model.py use the line below
    #success_url = "/shows/"

#Allows the user to update/change an existing Show object
class ShowUpdateView(UpdateView):
    template_name = "shows/show_create.html/"
    form_class = ShowsForm
    queryset = Show.objects.all()


    #Method that returns the object corresonding to an id
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Show, id=id)


#Allows the user to delete an existing Show object
class ShowDeleteView(DeleteView):
    template_name = "shows/show_delete.html/"
    queryset = Show.objects.all()
    
    #Must have success_url for DeleteView bc the default is show_detail.html but the object no longer exists
    def get_success_url(self):
        return reverse('shows:show-list')


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Show, id=id)
