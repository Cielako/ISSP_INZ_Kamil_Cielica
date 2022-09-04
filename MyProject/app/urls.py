from django.urls import path
from . import  views

# Ścieżki z których korzysta główny moduł 
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
