# thirdapp/views.py

from django.shortcuts import HttpResponse

def contact(request):
    return HttpResponse("Welcome to the contact page of Thirdapp!")

def faq(request):
    return HttpResponse("This is the FAQ page of Thirdapp!")
