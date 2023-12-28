# This file has been created manually inside the fees application
# this url file code has been copied from the main application i.e. from project4 > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/', views.fees_django),
    path('feespy/', views.fees_python),
]