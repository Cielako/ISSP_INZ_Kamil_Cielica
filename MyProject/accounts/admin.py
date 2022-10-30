from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.
class CustomAccountAdmin(UserAdmin):
    readonly_fields=('last_login',)
    list_display = ('username', 'email', 'last_login', 'is_staff')
    
    fieldsets = (
        ('Dane logowania',
            {
                'fields':(
                    'username',
                    'email',
                    'password',
                )
        }),
        ('Dane kontaktowe', 
            {
                'fields':(
                    'first_name',
                    'last_name',
                    'phone'
                )
        }),
         ('Uprawnienia',
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
        }),
          ('Logi', 
            {
                'fields':(
                    'last_login',
                    'date_joined',
                )
        }),
        
    )    
    
admin.site.register(Account, CustomAccountAdmin)

# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'last_login')
