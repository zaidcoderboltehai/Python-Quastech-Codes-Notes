from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
# from .models import *
from django.contrib.auth.models import User

def home(request):
    return render(request,"home.html")

def loginuser(request):
    if(request.method=="POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        
        return render(request,"login.html")
    
    else:
        return render(request,"login.html")

def addUser(request):
    if(request.method=="POST"):
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        # Hash the password
        hashed_password=make_password(password)

        user=User.objects.create(
            first_name=fname,
            last_name=lname,
            username=email,
            email=email,
            password=hashed_password
        )
        return redirect("/")
    
    else:
        return render(request,"adduser.html")
    
def list(request):
    users=User.objects.all()
    return render(request,"list.html",{"users":users})

def delete(request):
    id=request.GET.get("id")
    user=User.objects.get(id=id)
    user.delete()
    return redirect("/list")

def delete2(request,pk):
    user=User.objects.get(id=pk)
    user.delete()
    return redirect("/list")

def edit(request,pk):
    user=User.objects.get(id=pk)
    if(request.method=="POST"):
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user.name=name
        user.phone=phone
        user.email=email
        user.password=password
        user.save()
        return redirect("/list")
    else:
        return render(request,"editform.html",{"user":user})

def search(request):
    srch=request.GET.get("srch")
    users=User.objects.filter(name__contains=srch)
    return render(request,"list.html",{"users":users})

