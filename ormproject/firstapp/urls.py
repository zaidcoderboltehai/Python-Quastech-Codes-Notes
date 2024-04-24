from django.urls import path
from . import views as v
urlpatterns = [
    path("",v.loginuser),
    path("home",v.home),
    path("add-user",v.addUser),
    path("list",v.list),
    path("delete",v.delete),
    path("delete2/<int:pk>",v.delete2),
    path("edit/<int:pk>",v.edit),
    path("search",v.search)
]