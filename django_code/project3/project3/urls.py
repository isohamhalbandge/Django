"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importing
from course import views as course_views
from fees import views as fees_views

# another option
# from course.views import learn_django
# from fees.views import fees_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', course_views.learn_django),
    path('feesdj/', fees_views.fees_django),
]
