from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from .forms import RegistrationForm

User = get_user_model()


def registration_view(request):
    if request.user.is_authenticated:
        redirect('home')

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, 'Registration successful...')
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', context={'form': form,})
