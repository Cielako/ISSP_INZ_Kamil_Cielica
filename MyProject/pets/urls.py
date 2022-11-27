from django.urls import path
from . import views

# Argument w pasku url /<nazwa_argumentu> lub ?nazwa_argumentu
# Który zdefiniowaliśmy w funkcji danego widoku.

urlpatterns = [
    path('my-pets/', views.my_pets, name='my_pets'),
    path('my-pets/add-profile/', views.add_pet_profile, name='add_pet_profile'), 
    path('profile/<int:pet_id>', views.pet_profile, name='pet_profile'),
    path('profile/', views.pet_profile, name='pet_profile'),
    path('delete-profile/?pet_id', views.del_pet_profile, name='del_pet_profile'),
    path('edit-profile/<int:pet_id>/', views.edit_pet_profile, name='edit_pet_profile')
    
   
]
