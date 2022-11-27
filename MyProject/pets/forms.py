from django import forms
from .models import PetProfile

class PetRegisterForm(forms.ModelForm):
    pet_num = forms.CharField(
        required=True,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        error_messages = {
                'unique' : "Taki numer chipa już istnieje.",
                'max_length':"Wprowadzony numer chipa jest za długi."
                 })
    pet_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        error_messages = {
                'max_length':"Wprowadzona nazwa jest za długa"
                 })
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
        fields=['pet_num','pet_name', 'pet_desc', 'pet_image','is_lost']
    
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
    class Meta:
        model = PetProfile
        fields=['pet_num','pet_name', 'pet_desc', 'pet_image','is_lost']
    
    def save(self, commit: bool = True):
        """
        Edytuje i zapisuje obiekt bazodanowy z danych powiazanych
        z formularzem
        """
        pet = super(PetUpdateForm, self).save(commit=False)
        if commit:
            # pet.pet_num = self.cleaned_data['pet_num']
            # pet.pet_name = self.cleaned_data['pet_name']
            # pet.pet_desc = self.cleaned_data['pet_desc']
            # pet.pet_image = self.cleaned_data['pet_image']
            # pet.is_lost = self.cleaned_data['is_lost']
            pet.save()
        return pet