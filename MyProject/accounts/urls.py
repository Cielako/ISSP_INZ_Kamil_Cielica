from unicodedata import name
from django.urls import path
from . import  views

# Ścieżki z których korzysta główny moduł 
urlpatterns = [
    # {% url 'login' %} - pozwala na skrótowe odnośniki w html
    # Zapamiętać jeśli po zmianie path nie działa można dopisać user_...
    path('login', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout' ),
    path('profile', views.user_profile, name='profile' ),
    path('profile-edit', views.user_profile_edit, name='profile_edit'),
    path('password-change',views.user_password_change, name='password_change')
    
]
