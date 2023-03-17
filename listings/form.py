from django.forms import ModelForm,Form
from .models import Listings

class ListingForm(ModelForm):
    class Meta:
        model=Listings
        fields="__all__"