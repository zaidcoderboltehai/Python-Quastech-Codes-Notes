from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def loginpage(request):
    return render(request, "login.html")

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