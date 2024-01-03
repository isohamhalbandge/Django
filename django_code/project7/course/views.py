from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    # return HttpResponse("<h1>Hello Django</h1>")
    # making this dynamic 
    cname = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {
        'nm' : cname,
        'du' : duration,
        'st' : seats
    }
    # course_name = {
        # 'cname' : 'React'
    # }
    return render(request, 'course/courseOne.html', context=django_details) 

def learn_python(request):
    # return HttpResponse("<h1>Hello Python</h1>")
    return render(request, 'course/courseTwo.html') 