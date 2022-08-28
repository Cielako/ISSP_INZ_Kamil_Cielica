from django.urls import path
from . import  views

# Ścieżki z których korzysta główny moduł i
urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    
]
