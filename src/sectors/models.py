from django.db import models
from django.urls import reverse

# This table lists industry sectors that the client may be associated with
class Sector(models.Model):
    sector_name = models.TextField(blank = False, null = False)
    description = models.TextField(blank = True, null = True)

    #Get absolute url method
    def get_absolute_url(self):
        return reverse("sectors:sector-detail", kwargs={"id": self.id})

    #To show the attribute sector_name in the sector field of the /admin/clients/ page
    def __str__(self):
        return self.sector_name

