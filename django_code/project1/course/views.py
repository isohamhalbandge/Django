from django.shortcuts import render

# Importing the modules
from django.http import HttpResponse

# Create your views here.

# Creating my own views
def learn_django(request):
    return HttpResponse("<h1>Hello Django!</h1>")