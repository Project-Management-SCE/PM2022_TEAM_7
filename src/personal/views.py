from django.shortcuts import render


# Create your views here.

def home_screen_view(request):
    context = {}
    return render(request, "personal/home.html")


def Sourcesofknowledge_view(request):
    context = {}
    return render(request, "personal/Sourcesofknowledge.html")


def customersatisfactionsurvey_view(request):
    context = {}
    return render(request, "personal/customersatisfactionsurvey.html")
