import os
from queue import Empty
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, PetProfile, clean_old_image, delete_profile_dir

# Import formularzy
from .forms import PetRegisterForm, PetUpdateForm

# Import Paginacji 
from django.core.paginator import Paginator

# Create your views here.

# Wykonujemy zapytanie o listę zwierząt danego użytkownika
def my_pets(request):
    pet_list = PetProfile.objects.filter(owner_id=request.user.id).order_by('-add_date')
    
    p = Paginator(pet_list, 1) 
    page = request.GET.get('page')
    pets = p.get_page(page)
    
    if pets is None:
        return render(request, 'pet/my_pets.html')
    else: 
        return render(request, 'pet/my_pets.html', {'list' : pets })

# Zapytanie o profil danego zwierzęcia (*pet_num i *pet_id - argumenty opcjonalne)
def pet_profile(request, pet_num=None, pet_id=None):
    
    if request.method == "POST":
        pet_num = request.POST.get('check_number') 
        specific_data = PetProfile.objects.filter(pet_num=pet_num)
    elif  request.method == "GET":
        # pet_id = request.GET.get('pet_id')
        specific_data = PetProfile.objects.filter(id=pet_id)
    
    if specific_data:
        return render(request, 'pet/profile.html', {'all' : specific_data})
    else:
        messages.error(request, 'Zwierze o podanym numerze nie istnieje')  
        return  redirect("/")
       
# Dodaje nowe zwierze dla aktualnie zalogowanego użytkowinka    
def add_pet_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PetRegisterForm(request.POST, request.FILES)
            
            if form.is_valid():
                obj = form.save(commit=False)
                obj.owner_id = request.user.id
                obj.save()
                messages.success(request, 'Dodano nowe zwierzę')
                return redirect('my_pets')
            else:
                messages.error(request, 'Nie możesz dodać zwierzęcia taki numer już istnieje')
        else:
            form = PetRegisterForm()
        return render(request, 'pet/add_pet.html', context={'form':form})    
    else:
        messages.error(request, 'Nie możesz zarejestrować zwierzęcia, musisz być zalogowany.')
        return redirect('/')
    
# Edytuje dane zwierze danego użytkownika    
def edit_pet_profile(request, pet_id):
    profile = PetProfile.objects.get(pk=pet_id)
    
    if request.user.is_authenticated and request.user.id == profile.owner_id:
        if request.method == 'POST':
            form = PetUpdateForm(request.POST, request.FILES, instance=profile)
            if 'pet_image' in form.changed_data:
                clean_old_image(profile.pet_image)
                
            if form.is_valid():
                form.save()
                messages.success(request, 'Pomyślnie edytowano zwierzę')
                return redirect('my_pets')
            else:
                print(form.errors)
                messages.error(request, 'Wystąpił błąd przy edycji profilu.')
        else:
            form = PetUpdateForm(instance=profile)
        return render(request, 'pet/edit_profile.html', context={'form':form})
        #     messages.success(request, 'Pomyślnie usunięto zwierzę')
    else:
        messages.error(request, 'Nie masz dostępu do tej strony')
        return redirect('/')
        
# Usuwa  wybrane zwierze jeżeli użytkownik jest jego właścicielem   
def del_pet_profile(request, pet_id=None):
    if request.method == 'GET':
        pet_id = request.GET.get('pet_id')
        profile = PetProfile.objects.get(pk=pet_id)
        
        if request.user.id == profile.owner_id:
            delete_profile_dir(profile.pet_image)
            profile.delete()
            messages.success(request, 'Pomyślnie usunięto zwierzę')
        else:
            messages.error(request, 'Nie masz dostępu do tej strony')
    return redirect('my_pets')



# def add_pet_profile(request):
#     if(request.user.is_authenticated):
#         if request.method == 'POST':
#             form = PetRegisterForm(request.POST, request.FILES)
#             form.owner = request.user.id
#             print(form.cleaned_data)
#             if form.is_valid():
                
#                 print("test")
#                 form.save()
#             else:
#                 print(form.errors)
#         else:
#             form = PetRegisterForm()
#         return render(request, 'pet/add_pet.html', context={'form':form})
                
#     else:
#         messages.error(request, 'Nie możesz zarejestrować zwierzęcia, musisz być zalogowany.')
#         return redirect('/')