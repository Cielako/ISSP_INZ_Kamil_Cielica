from django.urls import path
from . import views

# Argument w pasku url dopisujemy do ścieżki /<nazwa_argumentu> 
# Który zdefiniowaliśmy w funkcji danego widoku.

urlpatterns = [
    path('my_pets/', views.my_pets, name='my_pets'), 
    path('profile/<int:pet_num>', views.pet_profile, name='pet_profile'),
    path('profile/', views.pet_profile, name='pet_profile'),
   
]
