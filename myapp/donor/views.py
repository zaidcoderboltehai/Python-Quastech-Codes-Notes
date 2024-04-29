from django.shortcuts import render

def donorhome(reqeust):
    return render(reqeust,'donorhome.html')

def addFood(request):
    if request.method=="POST":
        pass
    else:
        return render(request,'addfood.html')