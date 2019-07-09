from django import forms

from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "client_name",
            "client_city",
            "client_state",
            "client_since",
            "phone_number",

        ]
        
    #For validation functions, the func. name must be exactly below:
    #clean_<exactFunctionName>
    def clean_client_state(self):
        state = self.cleaned_data.get("client_state")
        if len(state) != 2:
            raise forms.ValidationError("Please enter a state abbreviation with two letters")
            print(len(state))
        if state.isalpha() != True:
            raise forms.ValidationError("Please enter a valid state abbreviation")
        return state


