from django.db import models
from django.urls import reverse

# Model to represent a show
class Show(models.Model):
    show_name = models.TextField(blank = False, null = False)
    client_name = models.TextField(blank = False, null = False)
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.TextField(blank = False, null = False)
    state = models.TextField(blank = False, null = False)

    #Get absolute url method
    def get_absolute_url(self):
        return reverse("shows:show-detail", kwargs={"id": self.id})
    

