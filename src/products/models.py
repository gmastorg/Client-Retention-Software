from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length is required
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    size = models.TextField(blank = False, null = False)
    active = models.BooleanField()
    # if blank is false, it is required input on the web page, null relates to the db
    # if blank is true, the textbox can be left blank on the web page when the object is created