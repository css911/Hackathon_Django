# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#method used for returning student registration page
def reg(request):
	return render(request,"register.html",{})

#method used for returning login page
def login(request):
	return render(request,"login.html",{})



#method used for returning password resetting page
def rest_password(request): 
	return render(request,"forgot_password.html",{})

#method used for returning teacher registration page
def regt(request):
	return render(request,"register_as_teacher.html",{})



