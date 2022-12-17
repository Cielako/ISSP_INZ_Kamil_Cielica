from django.contrib import admin
from .models import PetProfile

# Register your models here.

class PetProfileAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'chip_number', 
                    'desc', 'is_lost',
                    'phone','email', 'add_date')
    
admin.site.register(PetProfile, PetProfileAdmin)