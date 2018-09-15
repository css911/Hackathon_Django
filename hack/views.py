# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from models import Teacher,Student,Attendance_Sheet,Subject,Total_No_of_Classes,Info_of_allocation
from django.shortcuts import render_to_response
from django.template import RequestContext
#import pymsgbox

# Create your views here.

#method used for returning student registration page
@csrf_exempt
def reg(request):
	context={}
	#context["msg"]
	if request.method == "GET":
		print "Here"
		return render(request,"register.html",{})
	else :	
		print "Ok"
		fname=request.POST['fname']
		lname=request.POST['lname']
		password=request.POST['pass1']
		email=request.POST['em']
		phone=request.POST['phone']
		year=request.POST['year']
		roll=request.POST['roll']
		
		if Student.objects.filter(email=email).exists():
			print "already exists"
			return redirect('/register/')
			#return redirect('/login/')
		else :
			print "Here1"
			aaa=Student(First_Name=fname,Last_Name=lname,
				 email=email,
				 phone_number=phone, 
				 password=password,
				 Year=year,
				 Roll_No=roll
				 	)
			aaa.save()
			bbb=Attendance_Sheet(Roll_No=roll,sub1Att="0",sub2Att="0",
				sub3Att="0",sub4Att="0",sub5Att="0")
			bbb.save()
			print "Here2"
			#print typeuser
		return redirect('/log/')	

#method used for returning login page
@csrf_exempt
def login(request):

	if "email" in request.session :
		tu = request.session['typeuser']
		if tu == "student":
			return redirect('/student_dashboard/')
		elif tu == "authority":
			return redirect("/authority_dashboard/")	
		else:
			return redirect('/teacher_dashboard/')
	if request.method == "GET":
		return render(request,"login.html",{})
	else :	
		email=request.POST['email']
		passw=request.POST['pass']
		if Student.objects.filter(email=email).exists():
			user_obj=Student.objects.get(email=email)
			if user_obj.password == passw :
				request.session["email"] = email
				request.session["typeuser"] ="student"
				print "logged in "+user_obj.First_Name
				return redirect('/student_dashboard/')		
			else:
				print "wrong password"
				pymsgbox.alert('Wrong Password :(', 'Title')
				return redirect('/log/')	
		elif Teacher.objects.filter(email=email).exists():	
			user_obj=Teacher.objects.get(email=email)
			if user_obj.password == passw :
				request.session["email"] = email
				request.session["typeuser"] ="teacher"
				print "logged in "+user_obj.First_Name
				if user_obj.email == "Authority@gmail.com":
					request.session["typeuser"]="authority"
					return redirect('/authority_dashboard/')
				return redirect('/teacher_dashboard/')		
			else:
				print "wrong password"
				#pymsgbox.alert('Wrong Password :(', 'Title')
				return redirect('/log/')
		else:		
			print "User doesn't exist"
			return redirect('/log/')


@csrf_exempt
def auth_dash(request):
	if  "email" not in request.session:
		return redirect("/log/")
	elif request.session['typeuser'] != "authority":
		return redirect("/log/")

	context={}
	#if request.method == "GET":
	obj=Teacher.objects.all().exclude(email="Authority@gmail.com")
	context['teachers']=obj	
		
	return render(request,"auth_dash.html",context)		
		#return render_to_response('auth_dash.html', {},context_instance=RequestContext(request))
        
		
	#else:
	#	return render(request,"auth_dash.html",context)	
        

		







	




@csrf_exempt	
def logout(request):
	if "email" in request.session:
		del request.session['email']
	return redirect('/log/')





@csrf_exempt
def student_dash(request):
	if  "email" not in request.session:
		return redirect("/log/")
	elif request.session['typeuser'] != "student":
		return redirect("/log/")

	return render(request,"student_dashboard.html",{})	

@csrf_exempt
def teacher_dash(request):
	context={}
	if  "email" not in request.session:
		return redirect("/log/")
	elif request.session['typeuser'] != "teacher":
		return redirect("/log/")

	email = request.session['email']	
	obj = 	Info_of_allocation.objects.filter(email=email)	
	context['classes']=obj
	return render(request,"teacher_dashboard.html",context)	


#method used for returning password resetting page
@csrf_exempt
def rest_password(request): 
	return render(request,"forgot_password.html",{})


#method used for returning teacher registration page
@csrf_exempt
def regt(request):
	context={}
	#context["msg"]
	if request.method == "GET":
		print "Here"
		return render(request,"register_as_teacher.html",{})
	else :	
		print "Ok"
		fname=request.POST['fname']
		lname=request.POST['lname']
		password=request.POST['pass1']
		email=request.POST['em']
		phone=request.POST['phone']
		#year=request.POST['year']
		#roll=request.POST['roll']
		
		if Teacher.objects.filter(email=email).exists():
			print "already exists"
			return redirect('/register/')
			#return redirect('/login/')
		else :
			print "Here1"
			aaa=Teacher(First_Name=fname,Last_Name=lname,
				 email=email,
				 phone_number=phone, 
				 password=password
				 	)
			aaa.save()
			print "Here2"
			#print typeuser
		return redirect('/log/')	


@csrf_exempt
def class_alloc(request):
	context={}
	id=request.GET["teacher_id"]
	teacher_obj=Teacher.objects.get(id=id)
	#context['name']=teacher_obj
	#request.session['teacher_obj']=teacher_obj
	return render(request,"class_allocation.html",context)

@csrf_exempt
def dash(request):
	return render(request,"dash.html",{})