from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

# Definiujemy własne formularze coś na wzór tych w html

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=35, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=35, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=35, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=65, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model  = Account
        fields = ['username', 'email', 'password1', 'password2', 'phone']
        
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
        return user