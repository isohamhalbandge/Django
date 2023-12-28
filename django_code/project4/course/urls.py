# This file has been created manually inside the course application
# this url file code has been copied from the main application i.e. from project4 > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
]