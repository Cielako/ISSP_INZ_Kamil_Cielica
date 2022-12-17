import os
import shutil
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField 

from accounts.models import Account

# Create your models here.

# Tutaj Tworzymy model - czyli pojedyńczą porcje informacji o danych
# Zawiera podstawowe pola i zachowania danych które przechowujemy
# Każdy model jest mapowany na pojedyńcza tabelę bazy danych 
User = get_user_model()

def get_profile_image_filepath(self, filename):
    # return f'profile_images/{self.pk}/{"profile_image.png"}'
    return f'profile_images/{self.owner}/{self.chip_number}/"profile_pic.png"'
    

def get_default_profile_image():
    return "media/profile_images/def_profile_pic.png"

    """
    Funkcja usuwa poprzednie zdjęcie przesłane przez użytkownika
    """
def clean_old_image(instance):
    try:
        path = instance.path
        print("Pomyślnie Edytowano zdjęcie profilu")
        os.remove(path)
    except:
        print("Podano złą ścieżkę do pliku")

def delete_profile_dir(instance):
    try:
        path = str(instance.path).replace('\profile_pic.png','')
        shutil.rmtree(path)
    except:
        print("Podano złą ścieżkę do folderu")
      

# Profil zwierzęcia 
''' Model Profilu oznakowanego zwierzęcia '''
class PetProfile(models.Model):
    
    class Gender(models.TextChoices):
        M='Samiec', _('Samiec')
        F='Samica',_('Samica')
        
    class Type(models.TextChoices):
        G='Gryzoń', _('Gryzoń')
        GA='Gad', _('Gad')
        K='Kot', _('Kot')
        P='Pies', _('Pies')
        PT='Ptak', _('Ptak')
        I='Inny', _('Inny')
        
    owner = models.ForeignKey(User, verbose_name='właściciel zwierzęcia', default=1, blank=True, on_delete=models.CASCADE)
    chip_number = models.CharField(verbose_name='numer chipu', max_length=15, unique=True)
    pet_name = models.CharField(verbose_name='imię zwierzęcia', max_length=30)
    pet_type = models.CharField(verbose_name='Gatunek', max_length=6, choices=Type.choices, default=Type.G)
    gender = models.CharField(verbose_name='płeć', max_length=13, choices=Gender.choices, default=Gender.M)
    desc = models.TextField(verbose_name='opis zwierzęcia', max_length=500)
    image = models.ImageField(verbose_name='zdjęcie', max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)    
    is_lost = models.BooleanField(verbose_name='status zaginięcia', default=False)
    region = models.CharField(verbose_name='województwo', max_length=19, blank=False, choices=Account.RegionChoices.choices)
    add_date = models.DateField(verbose_name='data dodania', auto_now_add=True)
    
    
    
    def __str__(self):
        return self.chip_number
    
    @property # Własności z modelu User
    def email(self):
        return self.owner.email
    @property 
    def phone(self):
        return self.owner.phone
    # @property 
    # def region(self):
    #     return self.owner.region

