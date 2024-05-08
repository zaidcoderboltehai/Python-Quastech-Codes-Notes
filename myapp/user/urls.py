from django.urls import path
from .import views as v


urlpatterns = [
    path("userhome",v.home),
    path("viewfood/<int:pk>",v.foodView),
    path("sendrequest/<int:pk>",v.send_request)
]
