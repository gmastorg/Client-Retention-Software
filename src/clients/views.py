from django.shortcuts import render, get_object_or_404, redirect
from django.views import  View
from django.urls import reverse

from .models import Client

from .forms import ClientForm

# Turning a function based view into a class based view
#Any custom Class view inherits from View

#BE AWARE THAT CHANGES TO /CLIENTS/ whether adding or deleting are not immediately
#showing up in browser even after refreshing.... changes HAVE been made, just not showing

#This is raw code to understand how the Class based views (used for Shows) works in detail
#Class based views should be used instead, this is just for leanrning purposes



#Mixins allows extension of a class based view
class ClientObjectMixin(object):
    model = Client
    lookup = "id"

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id = id)
        return obj


#This class allows the user to create a new Client object
class ClientCreateView(View):
    template_name = "clients/client_create.html"
    def get(self, request, *args, **kwargs): #This would be get bc it is "getting"/rendering a template
        #GET METHOD
        form = ClientForm()
        context= {"form": form}
        return render(request, self.template_name, context)   #Get is the default, use post to submit data

    def post(self, request, *args, **kwargs):
        #POST METHOD
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
            #form = ClientForm() #This rerenders the form with no text in boxes, clean form.
        context= {"form": form}
        return render(request, self.template_name, context)

#This class allows the user to update/change an existing Client object
class ClientUpdateView(ClientObjectMixin, View):
    template_name = "clients/client_update.html"
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Client, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs): #This would be get bc it is "getting"/rendering a template
        #GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ClientForm(instance= obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)   #Get is the default, use post to submit data

    def post(self, request, id=None, *args, **kwargs):
        #POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ClientForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context["object"] = obj
            context["form"] = form
            return redirect(reverse("clients:client-detail", kwargs={"id": obj.id}))
        return render(request, self.template_name, context)


class ClientDeleteView(ClientObjectMixin, View):
    template_name = "clients/client_delete.html"
        
    def get(self, request, id=None, *args, **kwargs): #This would be get bc it is "getting"/rendering a template
        #GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)   #Get is the default, use post to submit data

    def post(self, request, id=None, *args, **kwargs):
        #POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context["object"] = None
            return redirect('/clients/')
        return render(request, self.template_name, context)


#Shows details of a specific Client object
class ClientView(ClientObjectMixin, View):
    template_name = "clients/client_detail.html"
    def get(self, request, id=None, *args, **kwargs): #This would be get bc it is "getting"/rendering a template
        context= {"object": self.get_object}
        return render(request, self.template_name, context)   #Get is the default, use post to submit data

#Shows a list of all Client objects
class ClientListView(View):
    template_name = "clients/client_list.html"
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)



