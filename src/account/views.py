from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import *
from user_profile.models import UserProfile


def home(request):
    return render(request, 'account/home.html')


def customersatisfactionsurvey(request):
    return render(request, 'account/customersatisfactionsurvey.html')


def Sourcesofknowledge(request):
    return render(request, 'account/Sourcesofknowledge.html')


def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            login(request, user)
            return redirect('account:home')
    else:
        form = UserCreateForm()
    return render(request, 'account/signup.html', {'form': form})

def map(request):
    return render(request, 'account/map.html')
