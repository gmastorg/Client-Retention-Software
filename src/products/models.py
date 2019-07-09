from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length is required
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    size = models.TextField(blank = False, null = False)
    active = models.BooleanField()
    # if blank is false, it is required input on the web page, null relates to the db
    # if blank is true, the textbox can be left blank on the web page when the object is created

    #Create instance method on model -"Getter Method", returns the url with the specified id
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"prod_id": self.id})
        # "product-detail" is the name of the url - see urls.py urlpatterns list
        #This function calls that url and sends in the kwargs