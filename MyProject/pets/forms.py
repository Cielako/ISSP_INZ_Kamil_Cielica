from django import forms
from .models import PetProfile
from accounts.models import Account

class PetRegisterForm(forms.ModelForm):
    pet_num = forms.CharField(
        required=True,
        max_length=15,
        widget=forms.NumberInput(attrs={'class': 'form-control'}), 
        error_messages = {
                'unique' : "Taki numer chipa już istnieje.",
                'max_length':"Wprowadzony numer chipa jest za długi."
                 }
        )
    
    pet_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=PetProfile.Type.choices)
    
    pet_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        error_messages = {
                'max_length':"Wprowadzona nazwa jest za długa"
                 })
    pet_sex = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=PetProfile.Sex.choices)
    
    pet_desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows":5, "cols":20 }),
        max_length=255,
        error_messages = {
                'max_length':"Wprowadzony opis zwierzęcia jest za długi"
                 }
    )
    pet_image = forms.ImageField(
        max_length=255,
        error_messages = {
                'max_length':"Wprowadzony opis zwierzęcia jest za długi"
                 })
    is_lost = forms.BooleanField(required=False)
    
    class Meta:
        model = PetProfile
        fields=['pet_num','pet_type','pet_name', 'pet_sex', 'pet_desc', 'pet_image','is_lost']
    
    def save(self, commit: bool = True):
        """
        Tworzy i zapisuje obiekt bazodanowy z danych powiazanych
        z formularzem
        """
        pet = super(PetRegisterForm, self).save(commit=False)
        if commit:
            # pet.pet_num = self.cleaned_data['pet_num']
            # pet.pet_name = self.cleaned_data['pet_name']
            # pet.pet_desc = self.cleaned_data['pet_desc']
            # pet.pet_image = self.cleaned_data['pet_image']
            # pet.is_lost = self.cleaned_data['is_lost']
            pet.save()
        return pet

class PetUpdateForm(PetRegisterForm):
    region = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=Account.RegionChoices.choices)
    
    class Meta:
        model = PetProfile
        fields=['pet_num','pet_type','pet_name', 'pet_sex','pet_desc', 'pet_image','is_lost', 'region'] 
        
    def save(self, commit: bool = True):
        """
        Edytuje i zapisuje obiekt bazodanowy z danych powiazanych
        z formularzem
        """ 
        pet = super(PetUpdateForm, self).save(commit=False)
        if commit:
            pet.save()
        return pet