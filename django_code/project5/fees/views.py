from django.shortcuts import render

# importing module
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    # return HttpResponse("<h1>300</h1>")
    return render(request, 'feesone.html')

def fees_python(request):
    # return HttpResponse("<h1>200</h1>")
    return render(request, 'feestwo.html')