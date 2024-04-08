from django.shortcuts import render,HttpResponse
data=[]
def home(request):
    return render(request,"home.html")

def register(request):
    return render(request,"form1.html")

def addDetails(request):
    name=request.GET.get("name")
    # name=request.GET["name"]
    city=request.GET.get("city")
    email=request.GET.get("email")
    password=request.GET.get("password")
    t=(name,city,email,password)
    data.append(t)
    return render(request,"display.html",{"user":t})

def register2(request):
    return render(request,"form2.html")

def addDetails2(request):
    name=request.POST.get("name")
    # name=request.GET["name"]
    city=request.POST.get("city")
    email=request.POST.get("email")
    password=request.POST.get("password")
    t=(name,city,email,password)
    data.append(t)
    return render(request,"display.html",{"user":t})

def alldata(request):
    return render(request,"alldata.html",{"data":data})


