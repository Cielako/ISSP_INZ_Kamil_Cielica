from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model  = Account
        fields = ('__all__')