
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from submit.models import User
# Create your views here.
#this function adds and show
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
        
    else:
        fm=StudentRegistration()   
    stud=User.objects.all() 
    return render(request,'base1.html',{'form':fm,'stu':stud})


#this function delete the data
def delete_data(request,id):
    if request.method=='POST':
        det=User.objects.get(pk=id)
        det.delete()
        return HttpResponseRedirect('/')



#this will update
def update_data(request,id):
    if request.method=='POST':
        up=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=up) 
        if fm.is_valid():
            fm.save()
    else:
        up=User.objects.get(pk=id)
        fm=StudentRegistration(instance=up) 

    return render(request,'updatestudent.html',{'form':fm})
     