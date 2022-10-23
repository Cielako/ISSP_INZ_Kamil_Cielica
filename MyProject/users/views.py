import imp
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, ("Jesteś zalogowany jako: " + user.get_username()))
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Wystąpił problem z zalogowaniem się :/"))
            return redirect('login')
    else:
        return render(request, 'auth/login.html')