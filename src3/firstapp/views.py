from django.shortcuts import HttpResponse,render

def home(request):
    return  render(request,"home.html")

def first(request):
    return render(request,"first.html")

def second(request):
    return render(request,"second.html")

