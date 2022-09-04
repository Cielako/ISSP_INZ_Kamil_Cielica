from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Definiujemy co ma nam zwrócić dany widok

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

