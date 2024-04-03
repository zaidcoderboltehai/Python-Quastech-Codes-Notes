from django.shortcuts import HttpResponse

def fourth(request):
    return  HttpResponse("welcome to fourth page")

def fifth(request):
    return HttpResponse("welcome to fifth page")