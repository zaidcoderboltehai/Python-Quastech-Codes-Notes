from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loginpage(request):
    if(request.method=="POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=email,password=password)
        if(user is not None):
            login(request,user)
            return redirect("/donorhome")
        else:
            return render(request, "login.html",{"msg":"invalid email or passowrd"})
    else:
        return render(request,"login.html")
    
def logoutuser(request):
    logout(request)
    return redirect("/")

def signup(request):
    if(request.method=="POST"):
        first_name=request.POST.get("firstName")
        last_name=request.POST.get("lastName")
        email=request.POST.get("email")
        password=request.POST.get("password")
        hashed_password=make_password(password)
        User.objects.create(username=email,email=email,first_name=first_name,password=hashed_password)
        return redirect("/")
    else:
        return render(request,"signup.html")

