from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserRegisterForm


# Testowa metoda do logowania się na stronie.
def user_login(request):
    """
        Autoryzacja użytkownika przez nazwę użytkownika lub adres e-mail
        
        Użytkownik może się zalogować, jeżeli użytkownik jest obecnie 
        zalogowany zostaje przekierowany na stronę główna witryny
        
    """
    if(request.user.is_authenticated):
        print('User already Authenticated')
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, ("Zalogowano się jako: " + user.get_username()))
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, ("Podane dane logowania nie są poprawne"))
                return redirect('login')
        else:
            return render(request, 'auth/login.html')
    
# Testowa Metoda do rejestracji - przykład metody z wykorzystaniem forms.py
def user_register(request):
    """
        Metoda pobiera dane z  formularza i tworzy nowy obiekt w bazie
    """
    if(request.user.is_authenticated):
        print('User already Authenticated')
        return redirect('/')
    else: 
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, 'Rejestracja Przebiegła pomyślnie')
                return redirect('/')
            else:
                messages.error(request, 'Rejestracja się nie powiodła, podano nieprawidłowe dane')
        form = UserRegisterForm()
        return render(request, 'auth/register.html', context={'form':form})
        
def user_logout(request):
    logout(request)
    return render(request, "index.html")