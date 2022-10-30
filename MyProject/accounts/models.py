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
    last_login = models.DateTimeField(verbose_name='ostatnio zalogowany', editable=False, auto_now=True)
    phone = PhoneNumberField(verbose_name='numer telefonu', null=False, blank=True)
    
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
