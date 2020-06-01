from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


def loginPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username ODER Passwort falsch!')

    return render(request, 'login.html', context)


def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():  # Checks if user is already taken etc, etc
            form.save()  # Create the user
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def homePage(request):
    context = {}

    return render(request, 'home.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
