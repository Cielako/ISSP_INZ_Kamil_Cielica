from atexit import register
from django.contrib import admin


# Register your models here.
# Możemy również dowolnie precyzować jak nasz model ma być wyświetlany 
''' Dajemy znać części administracyjnej Django, że nasz model jest 
    zarejestrowany używając spersonalizowanej klasy, która dziedziczy
    z ModelAdmin, można tutaj zamieścić informację jak wyświetlać ten 
    model na stronie i jak wejść z nim w interakcje
    
    admin.site.register(Profile) - domyślne ustawienie strony
'''
