from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_create_view(request):
    product_form = RawProductForm() #Initializes the form as request.GET
    if request.method == "POST":
        product_form = RawProductForm(request.POST) #request.POST here validates the input on the form
        if product_form.is_valid():
            print(product_form.cleaned_data)
            Product.objects.create(**product_form.cleaned_data)
        else:
            print(product_form.errors)
    context = {
        "form": product_form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)
    
    '''
    If there is a products directory with the file product_detail.html in both the "products" app
    folder and in the templates folder, the one in the templates folder overrides the one in the 
    "products" app folder. You can override any template that is in an app folder by placing a 
    new html template with the same name in the templates folder. This is because django is looking
    in the settings for the "DIR" filepath, which resolves to the "src's" templates folder.
    '''
