from django.db import models
from django.urls import reverse

# Model to represent a show
class Client(models.Model):
    client_name = models.TextField(blank = False, null = False)
    client_city = models.TextField(blank = True, null = True)
    client_state = models.TextField(blank = True, null = True)
    client_since = models.DateField()
    phone_number = models.TextField()

    #Get absolute url method
    def get_absolute_url(self):
        return reverse("clients:client-detail", kwargs={"id": self.id})
