from distutils.command.upload import upload
import email
from email.policy import default
from enum import unique
import imp
from operator import mod
from turtle import title
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 

# from django.utils import timezone
# from django.contrib.auth.models import User


# Create your models here.

# Tutaj Tworzymy model - czyli pojedyńczą porcje informacji o danych
# Zawiera podstawowe pola i zachowania danych które przechowujemy
# Każdy model jest mapowany na pojedyńcza tabelę bazy danych 

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "media/def_logo.png"

# Profil zwierzęcia 
''' Model Profilu oznakowanego zwierzęcia '''
class Profile(models.Model):
    email = models.EmailField(verbose_name="email", max_length=65, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    pet_id = models.CharField(max_length=15, unique=True)
    pet_name = models.CharField(max_length=30, unique=True)
    pet_desc = models.TextField(max_length=500)
    #pet_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_profile_image_filepath)    
    is_lost = models.BooleanField(default=False)
    
    def __str__(self):
        return self.pet_id
    
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
    