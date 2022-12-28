from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Definiujemy własne formularze coś na wzór tych w html

# Formularz rejestracji użytkownika
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=35, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'np. test123'}), 
        error_messages = {
                'unique' : "Taki użytkownik już istnieje.",
                'max_length':"Nazwa użytkownika jest za długa."
                 })
      
    email = forms.EmailField(
        max_length=65, 
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'np. test123@gmail.com'}),
        error_messages = {
                'unique' : "Podany adres e-mail już został wykorzystany.",
                'max_length':"adres e-mail jest za długi.",
                'invalid':"Podaj poprawny adres e-mail."
                })
    
    password1 = forms.CharField(
        max_length=35, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'*******'}),
        error_messages = {
                'min_length':"Podane hasło jest zbyt krótkie"
                })
    
    password2 = forms.CharField(
        max_length=35, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'*******'}))
    
    class Meta:
        model  = Account
        fields = ['username', 'email', 'password1', 'password2']
     
           
    def save(self, commit: bool = True):
        """
        Tworzy i zapisuje obiekt bazodanowy z danych powiazanych
        z formularzem
        """
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = False
        user.is_superuser = False
        
        if commit:
            user.save()
            # Nadajemy nowemu użytkownikowi uprawnienia do edycji użytkownika
            permission = Permission.objects.get(name='Can change user')
            user.user_permissions.add(permission)
        return user

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=35, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        required=False)
    
    last_name = forms.CharField(
        max_length=35, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        required=False)
    
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            initial="PL", 
            attrs={'class': 'form-control'}), required=False)
    
    region = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=Account.RegionChoices.choices)
    
    class Meta:
        model  = Account
        fields = ['first_name', 'last_name', 'phone', 'region']
   

class UserPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=35, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'*******'}))
    
    new_password2 = forms.CharField(
        max_length=35, 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'*******'}))
    
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']