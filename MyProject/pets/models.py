import os
import shutil
from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField 

# Create your models here.

# Tutaj Tworzymy model - czyli pojedyńczą porcje informacji o danych
# Zawiera podstawowe pola i zachowania danych które przechowujemy
# Każdy model jest mapowany na pojedyńcza tabelę bazy danych 
User = get_user_model()

def get_profile_image_filepath(self, filename):
    # return f'profile_images/{self.pk}/{"profile_image.png"}'
    return f'profile_images/{self.owner}/{self.pet_num}/"profile_pic.png"'
    

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
    owner = models.ForeignKey(User, verbose_name='właściciel zwierzęcia', default=1, blank=True, on_delete=models.CASCADE)
    pet_num = models.CharField(verbose_name='numer chipu', max_length=15, unique=True)
    pet_name = models.CharField(verbose_name='imię zwierzęcia', max_length=30)
    pet_desc = models.TextField(verbose_name='opis zwierzęcia', max_length=500)
    pet_image = models.ImageField(verbose_name='zdjęcie', max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)    
    is_lost = models.BooleanField(verbose_name='status zaginięcia', default=False)
    add_date = models.DateField(verbose_name='data dodania', auto_now_add=True)
    
    
    
    def __str__(self):
        return self.pet_num
    
    @property # Własności z modelu User
    def email(self):
        return self.owner.email
    @property 
    def phone(self):
        return self.owner.phone


