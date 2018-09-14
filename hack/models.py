# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Teacher(models.Model):
	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	#username = models.CharField(max_length=50,blank=False)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=50)
	password = models.CharField(max_length=50,blank=False)
	
	#MY_CHOICES = [('student', 'student'), ('teacher', 'teacher')]
	#typeuser= models.CharField(max_length=50,choices=MY_CHOICES)


	def __str__(self):
		return self.email+" "+self.password

class Student(models.Model):
	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	#username = models.CharField(max_length=50,blank=False)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=50)
	password = models.CharField(max_length=50,blank=False)
	Year = models.CharField(max_length=50)
	Roll_No =models.CharField(max_length=50)
	#MY_CHOICES = [('student', 'student'), ('teacher', 'teacher')]
	#typeuser= models.CharField(max_length=50,choices=MY_CHOICES)


	def __str__(self):
		return self.email+" "+self.password



