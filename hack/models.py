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

class Subject(models.Model):
	Year = models.CharField(max_length=50)
	sub1 = models.CharField(max_length=50)
	sub2 = models.CharField(max_length=50)
	sub3 = models.CharField(max_length=50)
	sub4 = models.CharField(max_length=50)
	sub5 = models.CharField(max_length=50)

	def __str__(self):
		return self.Year

class Attendance_Sheet(models.Model):
	Roll_No = models.CharField(max_length=50)
	sub1Att = models.CharField(max_length=50)
	sub2Att = models.CharField(max_length=50)
	sub3Att = models.CharField(max_length=50)
	sub4Att = models.CharField(max_length=50)
	sub5Att = models.CharField(max_length=50)

	def __str__(self):
		return self.Roll_No

class Total_No_of_Classes(models.Model):
	Year = models.CharField(max_length=50)
	Div  = models.CharField(max_length=50)
	Subject = models.CharField(max_length=50)
	Total_No = models.CharField(max_length=50)

	def __str__(self):
		return self.Year


class Info_of_allocation(models.Model):
	email = models.CharField(max_length=50)
	Year = models.CharField(max_length=50)
	Div = models.CharField(max_length=50)
	Subject = models.CharField(max_length=50)

	def __str__(self):
		return self.email


	













