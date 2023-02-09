from curses.ascii import HT
from multiprocessing import context
from queue import Empty
from django.shortcuts import render
from django.http import HttpResponse

from  pets.models import PetProfile
from  accounts.models import Account

# Definiujemy co ma nam zwrócić dany widok

def index(request):
    total_users = Account.objects.count()
    total_pets = PetProfile.objects.count()
    total_p_lost = PetProfile.objects.filter(is_lost=True).count()
   
    context = {
        'users': total_users,
        'pets': total_pets,
        'lost_pets':  total_p_lost
    }
    return render(request,'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

