from django.shortcuts import render

# importing
from django.http import HttpResponse

# Create your views here.

# custom functions
def learn_django(request):
    # return HttpResponse("<h1> Hello Django </h1>")
    return render(request, 'courseone.html')

def learn_python(request):
    # return HttpResponse("<h1> Hello Python </h1>")
    return render(request, 'coursetwo.html')

