"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hack import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),       #url mapping for the django admin page
    url(r'^register/',views.reg),           #url mapping for the student registration page
    

    url(r'^log/',views.login),              #url mapping for the login page
    url(r'^forgot-password/',views.rest_password),          #url mapping for the getting the forgot password page
    url(r'^logout/', views.logout),

    url(r'^register_as_teacher/',views.regt),         #url mapping for the register as teacher page

    url(r'^student_dashboard/',views.student_dash),             #url mapping for student dash

    url(r'^teacher_dashboard/',views.teacher_dash),             #url mapping for student dash

    url(r'^authority_dashboard/',views.auth_dash),             #url mapping for Authority

    url(r'^class_allocation/',views.class_alloc),

    url(r'^dash/',views.dash),
   
]
