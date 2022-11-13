from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, UserPasswordChangeForm


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
        messages.error(request, 'Nie możesz się zarejestrować, użytkownik jest już zalogowany.')
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
                error_list = [x for x in list(form.errors.values())[0]]
                counter = sum('password' in s for s in error_list)
                i=0
                for error in error_list:
                    if "password" in error:
                        i+=1
                        if i >= counter:
                            messages.error(request, 'Twoje hasło nie spełnia wymagań')
                    else:
                        messages.error(request, error)
                # error_list = [x for x in list(form.errors.values())[0] if x != "password"]
                # for error in error_list:
                #     if "password" in error:
                #         messages.error(request, 'Twoje hasło nie spełnia wymagań')
                #     else:
                #         messages.error(request, error)

                # messages.error(request, 'Rejestracja się nie powiodła, podano nieprawidłowe dane')
        else:
            form = UserRegisterForm()
        return render(request, 'auth/register.html', context={'form':form})
        
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def user_profile(request):
    if not (request.user.is_authenticated):
        messages.error(request, 'Zaloguj się, aby uzyskać dostęp do tej strony.')
        return redirect('/')
    else: 
        return render(request, 'auth/profile.html')

# @login_required(login_url='/')
def user_profile_edit(request):
    if not (request.user.is_authenticated):
        messages.error(request, 'Zaloguj się, aby uzyskać dostęp do tej strony.')
        return redirect('/')
    else: 
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Twój profil został edytowany pomyślnie.')
            else:
                messages.error(request, 'Wystąpił błąd przy edycji profilu.')
        else:
            form = UserUpdateForm(instance=request.user)
        return render(request, 'auth/profile_edit.html', context={'form':form})
    

def user_password_change(request):
    if not (request.user.is_authenticated):
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
        return render(request, 'auth/password_change.html', {'form': form})
        