from django.contrib import admin
from .models import PetProfile

# Register your models here.

class PetProfileAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_num', 
                    'pet_desc', 'is_lost',
                    'phone','email')
    
admin.site.register(PetProfile, PetProfileAdmin)