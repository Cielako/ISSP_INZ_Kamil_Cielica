from django.urls import path
from . import  views

# Ścieżki z których korzysta główny moduł 
urlpatterns = [
    # {% url 'login' %} - pozwala na skrótowe odnośniki w html
    path('user_login', views.user_login, name="login")
]
