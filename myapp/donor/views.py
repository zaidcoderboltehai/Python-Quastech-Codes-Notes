from django.shortcuts import render,redirect
from . models import *
def donorhome(request):
    foods=Food.objects.filter(donor=request.user)
    return render(request,"donorhome.html",{"foods":foods})

def addFood(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        expiry_date=request.POST.get("expiry_date")
        pickup_address=request.POST.get("pickup_address")
        image=request.FILES.get("image")
        donor=request.user
        food=Food(name=name,description=description,expiry_date=expiry_date,pickup_address=pickup_address,image=image,donor=donor)
        food.save()
        return redirect("/donorhome")
    else:
        return render(request,'addfood.html')
    
def deleteFood(request,pk):
    food=Food.objects.get(id=pk,donor=request.user)
    food.delete()
    return redirect("/donorhome")

def editFood(request,pk):
    food=Food.objects.get(id=pk,donor=request.user)
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        expiry_date=request.POST.get("expiry_date")
        pickup_address=request.POST.get("pickup_address")
        donor=request.user
        food.name=name
        food.description=description
        food.expiry_date=expiry_date
        food.pickup_address=pickup_address
        if (request.FILES):
            image=request.FILES.get("image")
            food.image=image
        food.donor=donor
        food.save()
        return redirect("/donorhome")
    else:
        return render(request,'editfood.html',{"food":food})
    

