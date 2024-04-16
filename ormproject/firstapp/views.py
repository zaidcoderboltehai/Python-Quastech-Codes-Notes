from django.shortcuts import render,HttpResponse,redirect
from .models import *
def home(request):
    return render(request,"home.html")

def addUser(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")

        print(name,phone,email,password)
        # return HttpResponse("success")
        user=User()
        user.name=name
        user.phone=phone
        user.email=email
        user.password=password
        user.save()
        return redirect("/")
    
    else:
        return render(request,"adduser.html")
    
def list(request):
    users=User.objects.all()
    return render(request,"list.html",{"users":users})
