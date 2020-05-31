from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def index(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): #Checks if user is already taken etc, etc
            form.save() #Create the user
            return redirect('/login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
