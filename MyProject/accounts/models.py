import email
from email.policy import default
from enum import auto, unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField 

# Rozszerzamy wbudowaną klasę AbstractBaseUser - model użytkownika
class Account(AbstractUser):
    # verbose_name - uzyskujemy więcej informacji w panelu administratora 
    # auto_now_add - ustawia datę w momencie utworzenia nowego obiektu
    
    
    username = models.CharField(verbose_name='nazwa użytkownika', max_length=35, unique=True)
    email = models.EmailField(verbose_name='adres email', max_length=65, unique=True)
    phone = PhoneNumberField(verbose_name='numer telefonu', null=False, blank=True)
    
    is_active = models.BooleanField(verbose_name='konto aktywne', default=True, help_text='Aktywność konta użytkownika')
    is_staff = models.BooleanField(verbose_name='administrator', default=False, help_text='Możliwość zalogowania do panelu administracyjnego')
    is_superuser = models.BooleanField(verbose_name='status SuperUsera', help_text='Użytkownik ma pełną kontrolę bez delegacji uprawnień')
    
    last_login = models.DateField(verbose_name='ostatnie logowanie', auto_now=True)
    
    
    # # Zamiast nazwy użytkownika logujemy się mailem
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    
    # # Ta metoda zwraca obiekt w postaci stringa
    # def __str__(self):
    #     return self.username
    
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    
    # def has_module_perms(self, app_label):
    #     return True
