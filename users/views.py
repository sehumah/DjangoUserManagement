from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse


def dashboard(request):
    return render(request, "users/dashboard.html", {})


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))


def dummy_page(request):
    return render(request, 'dummy_page.html', {})
