from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user) #returns the user that is currently logged in 
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    about_dict = {
        "about_text": "Our company has been creating awe-inspiring booths for expos since...",
        "about_list": ['chairs', 'posters', 'tables', 'lighting'],
        "about_bool": True, #See conditions in about.html, change this to test
        }

    return render(request, "about.html", about_dict)