from django.shortcuts import render, HttpResponse
from .models import myregister 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import datetime as dt
# Create your views here.
def home_page_view(request):
    return render (request,'home.html')

def staff_info_views(request):
    news1='Dr.Shalini Gambhir'
    news2='Ms.Mansi vats'
    news3='Mr.Alok mishra'
    news4='Mr.Meetender adhana'
    news5='Ms.Smriti Sharma'
    my_dict={"news1":news1,"news2":news2,"news3":news3,"news4":news4,"news5":news5}
    return render(request,'home1.html',my_dict)

def student_info(request):
    student1='Anmol Dhingra'
    student2='Badal Kumar'
    student3='Shivang Gulia'
    student4='Tarun Goyal'
    student5='Aryan Shivhare'
    my_dict1={"student1":student1,"student2":student2,"student3":student3,"student4":student4,"student5":student5}
    return render(request,'home2.html',my_dict1)

def event_info(request):
    event1='Farewell 2018'
    event2='Events 2022-23'
    event3='Events 2023-24'
    event4='GGSIPU Info Xpression'
    event5='Industrial visit'
    my_dict3={"event1":event1,"event2":event2,"event3":event3,"event4":event4,"event5":event5}
    return render(request,'home3.html',my_dict3)



def register(request):
    myreg=myregister()
    if request.method == "POST":
     
        # Retrieve form data
    
            fname = request.POST['fname']
            lname = request.POST['lname']
            course = request.POST['course']
            file = request.POST['file']
        
            # Create a new user
       
        
            myreg.fname = fname
            myreg.lname = lname
            myreg.course = course
            myreg.file = file
      

            myreg.save()
        
        

      

        # Handle other logic (e.g., activation email, redirect, etc.)

    # Render your registration template
            return HttpResponse("Submitted")
    return render(request,'register.html')
   





        



def scholarship(request):
   
    return render(request,'scholarship.html')


def infrastructure(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

    return render(request,'infrastructure.html')






# views.py




