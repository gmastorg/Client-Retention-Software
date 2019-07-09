from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# These are function based views


#Allows the user to create a new Product
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

    
    '''
    If there is a products directory with the file product_detail.html in both the "products" app
    folder and in the templates folder, the one in the templates folder overrides the one in the 
    "products" app folder. You can override any template that is in an app folder by placing a 
    new html template with the same name in the templates folder. This is because django is looking
    in the settings for the "DIR" filepath, which resolves to the "src's" templates folder.
    '''
#Allows user to enter a number in the URL to view the product_detail.html page of that object
def dynamic_lookup_view(request, prod_id):
    obj = get_object_or_404(Product, id= prod_id)
    context = {
        "object":obj
    }
    return render(request, "products/product_detail.html", context)

#Allows the user to delete an object
def product_delete_view(request, prod_id):
    obj = get_object_or_404(Product, id= prod_id)
    #Line below is confirming that the user WANTS to delete the item
    if request.method == "POST":
        #This is deleting the item
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }
    return render(request, "products/product_delete.html", context)

#Allows a user to update an object -- CURRENTLY NOT WORKING
def product_update_view(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)
    


#List all the objects in the Products table in product_list.html
#After an object is deleted, redirect here. TO DO - After a product is created, redirect here
def product_list_view(request):
    queryset = Product.objects.all() #Returns list of objects
    context = {
        "product_list": queryset
    }
    return render(request, "products/product_list.html", context)




