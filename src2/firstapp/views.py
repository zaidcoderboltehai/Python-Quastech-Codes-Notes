from django.shortcuts import HttpResponse

def first_view(request):
    return HttpResponse("Welcome to the first app!")

def second_view(request):
    return HttpResponse("Welcome to the second view of the first app!")
