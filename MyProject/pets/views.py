import os
from queue import Empty
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, PetProfile, clean_old_image, delete_profile_dir

from .utils import paginate

# Import formularzy
from .forms import PetRegisterForm, PetUpdateForm

# Import Paginacji 
from django.core.paginator import Paginator

#Import filtrów
from .filters import LostPetFilters


        
 # ----Tu renderujemy widoki --------------   

# Wykonujemy zapytanie o listę zwierząt danego użytkownika

def my_pets(request):
    pet_list = PetProfile.objects.filter(owner_id=request.user.id).order_by('-add_date')
    
    return paginate(request, pet_list, 'pets/my_pets.html', 4, )

    # p = Paginator(pet_list, 1) 
    # page = request.GET.get('page')
    # pets = p.get_page(page)
    
    # if pets is None:
    #     return render(request, 'pets/my_pets.html')
    # else: 
    #     return render(request, 'pets/my_pets.html', {'list' : pets })

# Zapytanie o profil danego zwierzęcia (*chip_number i *pet_id - argumenty opcjonalne)
def pet_profile(request, chip_number=None, pet_id=None):
    
    if request.method == "POST":
        chip_number = request.POST.get('check_number') 
        specific_data = PetProfile.objects.filter(chip_number=chip_number)
    elif  request.method == "GET":
        # pet_id = request.GET.get('pet_id')
        specific_data = PetProfile.objects.filter(id=pet_id)
    context = {'all' : specific_data}
    if specific_data:
        return render(request, 'pets/profile.html', context)
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
                obj.region = request.user.region
                obj.save()
                messages.success(request, 'Dodano nowe zwierzę')
                return redirect('my_pets')
            else:
                 messages.error(request, 'Wystąpił błąd przy dodawaniu zwierzęcia')
        else:
            form = PetRegisterForm()
            context={'form':form}
        return render(request, 'pets/add_pet.html', context)    
    else:
        messages.error(request, 'Nie możesz zarejestrować zwierzęcia, musisz być zalogowany.')
        return redirect('/')
    
# Edytuje dane zwierze danego użytkownika    
def edit_pet_profile(request, pet_id):
    profile = PetProfile.objects.get(pk=pet_id)
    
    if request.user.is_authenticated and request.user.id == profile.owner_id:
        if request.method == 'POST':
            form = PetUpdateForm(request.POST, request.FILES, instance=profile)
            if 'image' in form.changed_data:
                clean_old_image(profile.image)
                
            if form.is_valid():
                form.save()
                messages.success(request, 'Pomyślnie edytowano zwierzę')
                return redirect('my_pets')
            else:
                #messages.error(request, 'Wystąpił błąd przy edycji profilu.')
                 for value in form.errors:
                    # Zwracamy argument jako lista
                    messages.error(request, form.errors[value].as_ul())
        else:
            form = PetUpdateForm(instance=profile)
            context={'form':form}
        return render(request, 'pets/edit_profile.html', context)
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
            delete_profile_dir(profile.image)
            profile.delete()
            messages.success(request, 'Pomyślnie usunięto zwierzę')
        else:
            messages.error(request, 'Nie masz dostępu do tej strony')
    return redirect('my_pets')

# do poprawy paginacja i filtrowanie
def lost_pets(request):
    #-----------------------------------------------------
    # context = {}
    # listing = PetProfile.objects.filter(is_lost=True)
    # listing_filter = LostPetFilters(request.GET, queryset=listing)
   
    # context['listing_filter'] = listing_filter
    
    # pag_filtered_pets = Paginator(listing_filter.qs, 2)
    # page_number = request.GET.get('page')
    # pet_page_obj = pag_filtered_pets.get_page(page_number)
    # context['pet_page_obj'] = pet_page_obj
    # return render(request, "pets/lost_pets.html", context)
    listing = PetProfile.objects.filter(is_lost=True)
    listing_filter = LostPetFilters(request.GET, queryset=listing)
    return paginate(request, listing_filter, 'pets/lost_pets.html', 4, True )


    #------------------------------------------------------
    # listing = PetProfile.objects.filter(is_lost=True)
    # listing_filter = LostPetFilters(request.GET, queryset=listing)
    # p = Paginator(listing_filter.qs, 1) 
    # page = request.GET.get('page')
    
    # try: 
    #     pets = p.page(page)
    # except PageNotInteger:
    #     pets = p.page(p.num_pages)
    # listing_filter = LostPetFilters(request.GET, queryset=listing)
    # context = {
    #     'listing_filter' : pets
    # }
    # return render(request, "pets/lost_pets.html", context)


