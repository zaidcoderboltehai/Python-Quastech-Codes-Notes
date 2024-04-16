from django.urls import path
from . import views as v
urlpatterns = [
    path("",v.home),
    path("add-user",v.addUser),
    path("list",v.list)
]