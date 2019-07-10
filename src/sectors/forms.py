from django import forms
from .models import Sector

class SectorForm(forms.ModelForm):
    sector_name = forms.CharField()
    description = forms.Textarea()
    class Meta:
        model = Sector
        fields = [
                'sector_name',
                'description',
                ]