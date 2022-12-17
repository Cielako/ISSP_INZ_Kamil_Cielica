from curses.ascii import HT
from multiprocessing import context
from queue import Empty
from django.shortcuts import render
from django.http import HttpResponse
# from .models import User, Profile

# Definiujemy co ma nam zwrócić dany widok

def index(request):
    return render(request, 'index.html')

# Zwracamy informacje o danym profilu 
# def profile(request):
#     req_data = request.POST.get('check_number', None)
#     specific_data = Profile.objects.filter(chip_number=req_data).values()
#     if specific_data is not Empty:
#         return render(request, 'profile.html', {'all': specific_data})
#     else:
#         return render(request, 'profile.html', {'all': ['Nie ma takiego zwierzęcia :(']})  
    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

