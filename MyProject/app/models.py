from curses.ascii import US
from distutils.command.upload import upload
from email.policy import default
from operator import mod
from urllib import request
from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField 

# from django.utils import timezone
# from django.contrib.auth.models import User


# Create your models here.

# Tutaj Tworzymy model - czyli pojedyńczą porcje informacji o danych
# Zawiera podstawowe pola i zachowania danych które przechowujemy
# Każdy model jest mapowany na pojedyńcza tabelę bazy danych 
User = get_user_model()

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "media/def_profile_pic.png"

# Profil zwierzęcia 
''' Model Profilu oznakowanego zwierzęcia '''
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email', max_length=65)
    phone = PhoneNumberField(null=False, blank=False )
    pet_num = models.CharField(max_length=15, unique=True)
    pet_name = models.CharField(max_length=30)
    pet_desc = models.TextField(max_length=500)
    pet_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)    
    is_lost = models.BooleanField(default=False)
    
    def __str__(self):
        return self.pet_num
    
# class Post (models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published')
#     )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, 
#                             unique_for_date='publish')
#     author = models.ForeignKey(User, 
#                                on_delete=models.CASCADE,
#                                related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10,
#                             choices=STATUS_CHOICES,
#                             default='draft')
#     class Meta:
#         ordering = ('-publish',)
        
#     def __str__(self):
#         return self.title
    