from django import forms
from .models import Show

class ShowsForm(forms.ModelForm):
    show_name = forms.CharField()
    client_name = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    city = forms.CharField()
    state = forms.CharField()
    class Meta:
        model = Show
        fields = [
                'show_name',
                'client_name',
                'start_date',
                'end_date',
                'city',
                'state',
                ]

    def validate_date():
        pass

    def validate_state():
        pass