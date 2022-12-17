from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# Import Paginacji 
from django.core.paginator import Paginator

def paginate(request:HttpRequest, listing, template:str='index.html', psize:int=1, form_filtered:bool=False):
    """
    Tworzy paginator stron, w zaleożności od tego czy strona będzie filtrowana.

    Parametry
    ---------
    object_list : BaseManager[PetProfile]
        Lista obiektów do podziału na strony paginatora.
    template : str
        Ścieżka do strony mającej korzystać z paginatora.
    psize : int
        Liczba elementów wyświetlanych na stronie  
    Zwraca:
        HttpResponse: _description_
    """
    context = {}
    
    if form_filtered:
        print("Paginator z filtrowaniem")
        context['listing_filter'] = listing
        paginator = Paginator(listing.qs, psize)
       
    else:
        print("Paginator z bez filtrowania")
        paginator = Paginator(listing, psize)
    page = request.GET.get('page')
    page_list = paginator.get_page(page)
    context['pet_page_obj'] = page_list
    
    if page_list is None:
        return render(request, template)
    else:
        return render(request, template, context)
    
    # [---LOST_PETS OLD VIEW----]
    
    # context = {}
    # listing = PetProfile.objects.filter(is_lost=True)
    # listing_filter = LostPetFilters(request.GET, queryset=listing)
   
    # context['listing_filter'] = listing_filter
    
    # pag_filtered_pets = Paginator(listing_filter.qs, 2)
    # page_number = request.GET.get('page')
    # pet_page_obj = pag_filtered_pets.get_page(page_number)
    # context['pet_page_obj'] = pet_page_obj
    # return render(request, "pet/lost_pets.html", context)
