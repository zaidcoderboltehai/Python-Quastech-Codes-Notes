from django.shortcuts import HttpResponse

def third_view(request):
    return HttpResponse("Welcome to the third view of the second app!")

def fourth_view(request):
    return HttpResponse("Welcome to the fourth view of the second app!")
