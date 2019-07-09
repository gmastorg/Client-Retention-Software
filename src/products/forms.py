from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(required = True, label = 'Item Name',
    widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "title-box",
                "rows": 3,
                "cols": 30,

            }
        )),
    email = forms.EmailField()
    description = forms.CharField(
        widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "desc-box",
                "rows": 15,
                "cols": 60,

            }
        )) #Gives larger text box
    price = forms.DecimalField()
    size = forms.CharField(widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "size-box",
                "rows": 3,
                "cols": 30,

            }
        ))
    active = forms.BooleanField()
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price',
                'size',
                'active'
                ]


    #Input validation::: Ensure the title is more than one character
    def clean_client_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) <= 1:
            raise forms.ValidationError("Title must contain more than one character")
        return title

    #To use for another app::: Ensure the email address contains a "@" and "."
    #There is an email box on the form, but it is not being saved to the db
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not "@" in email or not "." in email:
            raise forms.ValidationError("Invalid email address")
        return email
            



#Not currently using this class, used for demo purposes
class RawProductForm(forms.Form):
    #Default for required is always True
    title = forms.CharField(required = True, label = 'Item Name',
    widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "title-box",
                "rows": 3,
                "cols": 30,

            }
        ))
    description = forms.CharField(
        widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "desc-box",
                "rows": 15,
                "cols": 60,

            }
        )) #Gives larger text box
    price = forms.DecimalField()
    size = forms.CharField(widget = forms.Textarea(
            attrs={
                "class": "input-box-class",
                "id": "size-box",
                "rows": 3,
                "cols": 30,

            }
        ))
    active = forms.BooleanField()

    