from django.urls import path
from . import views

# Argument w pasku url /<nazwa_argumentu> lub ?nazwa_argumentu
# Który zdefiniowaliśmy w funkcji danego widoku.

urlpatterns = [
    path('my_pets/', views.my_pets, name='my_pets'),
    path('my_pets/add_pet_profile/', views.add_pet_profile, name='add_pet_profile'), 
    path('profile?pet_id', views.pet_profile, name='pet_profile'),
    path('profile/', views.pet_profile, name='pet_profile'),
    path('delete_profile?pet_id', views.del_pet_profile, name='del_pet_profile')
    
   
]
