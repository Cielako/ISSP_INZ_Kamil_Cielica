from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Definiujemy co ma nam zwrócić dany widok

def home(request):
    return HttpResponse('<h1>App Home<h1>')

def about(request):
     return HttpResponse('<h1>App About<h1>')

