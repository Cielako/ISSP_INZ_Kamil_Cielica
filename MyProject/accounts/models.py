from django.utils.translation import gettext_lazy as _
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
    
    class RegionChoices(models.TextChoices):
        UNK='Inna lokalizacja', _('Inna lokalizacja')
        DS='Dolnośląskie', _('Dolnośląskie')
        KP='Kujawsko-pomorskie', _('Kujawsko-pomorskie')
        LB='Lubelskie', _('Lubelskie')
        LS='Lubuskie', _('Lubuskie')
        LD='Łódzkie', _('Łódzkie')
        MP='Małopolskie', _('Małopolskie')
        MZ='Mazowieckie', _('Mazowieckie')
        OP='Opolskie', _('Opolskie')
        PK='Podkarpackie', _('Podkarpackie')
        PL='Podlaskie',_('Podlaskie')
        PM='Pomorskie', _('Pomorskie')
        SL='Śląskie', _('Śląskie')
        SK='Świętokrzyskie', _('Świętokrzyskie')
        WP='Wielkopolskie', _('Wielkopolskie')
        WM='Warmińsko-mazurskie', _('Warmińsko-mazurskie')
        ZP='Zachodnio-pomorskie', _('Zachodnio-pomorskie')
    
    username = models.CharField(verbose_name='nazwa użytkownika', max_length=35, unique=True)
    email = models.EmailField(verbose_name='adres email', max_length=65, unique=True)
    phone = PhoneNumberField(verbose_name='numer telefonu', null=False, blank=True)
    region = models.CharField(verbose_name='województwo', max_length=19, blank=False, choices=RegionChoices.choices, default=RegionChoices.UNK)
    
    is_active = models.BooleanField(verbose_name='konto aktywne', default=True, help_text='Aktywność konta użytkownika')
    is_staff = models.BooleanField(verbose_name='administrator', default=False, help_text='Możliwość zalogowania do panelu administracyjnego')
    is_superuser = models.BooleanField(verbose_name='status SuperUsera', default=False, help_text='Użytkownik ma pełną kontrolę bez delegacji uprawnień')
    
    last_login = models.DateField(verbose_name='ostatnie logowanie', auto_now=True)
    
    
    # # Ta metoda zwraca obiekt w postaci stringa
    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
        return True
