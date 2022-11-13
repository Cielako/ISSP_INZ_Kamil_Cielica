from django.shortcuts import render
from .models import User, PetProfile
from queue import Empty
from django.http import HttpResponse

# Create your views here.

def my_pets(request):
    return render(request, 'pet/my_pets.html')
#opcjonalny argument *pet_num

def pet_profile(request, pet_num=None):
    
    if request.method == "POST":
        req_data = request.POST.get('check_number', None) 
        specific_data = PetProfile.objects.filter(pet_num=req_data).values()
    elif pet_num is not None:
        specific_data = PetProfile.objects.filter(pet_num=pet_num).values()
    
    if specific_data is not Empty:
        return render(request, 'pet/profile.html', {'all': specific_data})
    else:
        return render(request, 'pet/profile.html', {'all': ['Nie ma takiego zwierzęcia :(']})  