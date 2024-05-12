from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from donor.models import Food,Request

def foodView(request,pk):
    food=Food.objects.get(id=pk)
    return render(request,"viewfood.html",{"food":food})

def home(request):
    if request.user.is_staff:
        return redirect("/donorhome")
    foods=Food.objects.all()
    return render(request,"userhome.html",{"foods":foods})


def loginpage(request):
    if(request.method=="POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=email,password=password)
        if(user is not None):
            login(request,user)
            return redirect("/userhome")
        else:
            return render(request,"login.html",{"msg":"invalid email or password"})
    else:
        return render(request,"login.html")
    
def logoutuser(request):
    logout(request)
    return redirect("/")


def signup(request):
    if (request.method=="POST"):
        first_name=request.POST.get("firstName")
        last_name=request.POST.get("lastName")
        email=request.POST.get("email")
        password=request.POST.get("password")
        hashed_password=make_password(password)
        User.objects.create(username=email,email=email,first_name=first_name,password=hashed_password)
        return redirect("/")
    else:
        return render(request,"signup.html")
    
def send_request(request,pk):
    user=request.user
    food=Food.objects.get(id=pk)
    reqobj=Request()
    reqobj.user=user
    reqobj.food=food
    reqobj.save()
    return redirect("/userhome")
