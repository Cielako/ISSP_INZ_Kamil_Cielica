from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm, UserPasswordChangeForm


# Testowa metoda do logowania się na stronie.
def user_login(request):
    """
        Autoryzacja użytkownika przez nazwę użytkownika lub adres e-mail
        
        Użytkownik może się zalogować, jeżeli użytkownik jest obecnie 
        zalogowany zostaje przekierowany na stronę główna witryny
        
    """
    if(request.user.is_authenticated):
        messages.error(request, 'Użytkownik jest już zalogowany')
        return redirect('/')
    else:
        if request.method == "POST":
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                user = authenticate(request, 
                    username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request, ("Zalogowano się jako: " + user.get_username()))
                    return redirect('index')
            else:
                 for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == 'To pole jest wymagane.':
                        messages.error(request, "Musisz poprawnie przejść weryfikację reCAPTCHA.")
                        continue
                    messages.error(request, "Podane dane logowania nie są poprawne.") 
        else:
            form = UserLoginForm()
        return render(request, 'accounts/login.html', context={'form':form})
    
# Testowa Metoda do rejestracji - przykład metody z wykorzystaniem forms.py
def user_register(request):
    """
        Metoda pobiera dane z  formularza i tworzy nowy obiekt w bazie
    """
    if(request.user.is_authenticated):
        messages.error(request, 'Nie możesz się zarejestrować, użytkownik jest już zalogowany.')
        return redirect('/')
    else: 
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(request, 
                    username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password1'])
                login(request, user)
                messages.success(request, 'Rejestracja Przebiegła pomyślnie')
                return redirect('/')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == 'To pole jest wymagane.':
                        messages.error(request, "Musisz poprawnie przejść weryfikację reCAPTCHA")
                        continue
                    messages.error(request, error) 
                # for value in form.errors:
                #     print(form.errors[value].as_ul())
                #     messages.error(request, form.errors[value].as_ul())
        else:
            form = UserRegisterForm()
        return render(request, 'accounts/register.html', context={'form':form})
        
def user_logout(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany")
    return redirect('/')

def user_profile(request):
    if not (request.user.is_authenticated):
        messages.error(request, 'Zaloguj się, aby uzyskać dostęp do tej strony.')
        return redirect('/')
    else: 
        return render(request, 'accounts/profile.html')

# @login_required(login_url='/')
def user_profile_edit(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Zaloguj się, aby uzyskać dostęp do tej strony.')
        return redirect('/')
    else: 
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Twój profil został edytowany pomyślnie.')
                return redirect('profile')
            else:
                messages.error(request, 'Wystąpił błąd przy edycji profilu.')
        else:
            form = UserUpdateForm(instance=request.user)
        return render(request, 'accounts/profile_edit.html', context={'form':form})
    

def user_password_change(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Zaloguj się, aby uzyskać dostęp do tej strony.')
        return redirect('/')
    else:
        user = request.user
        if request.method == 'POST':
            form = UserPasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Twoje hasło zostało zmienione, zaloguj się nowym hasłem")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, "Twoje hasło nie spełnia wymagań")

        form = UserPasswordChangeForm(user)
        return render(request, 'accounts/password_change.html', {'form': form})
        