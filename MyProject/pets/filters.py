import django_filters
from django import forms
from .models import PetProfile
from accounts.models import Account

class LostPetFilters(django_filters.FilterSet):
    class Meta:
        model = PetProfile
        fields = {
            'pet_type': ['exact'], 
            'pet_sex' : ['exact'],
            'region' : ['exact']
        }
        widgets = {
            'pet_type' : forms.Select(attrs={'class':'form-control'})
        }