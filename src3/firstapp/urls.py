from django.urls import path
from . import  views as v
urlpatterns =[
    path('',v.home),
    path('register',v.register),
    path('add-details',v.addDetails),

    path('register2',v.register2),
    path('add-details2',v.addDetails2),

    path("alldata",v.alldata)

]