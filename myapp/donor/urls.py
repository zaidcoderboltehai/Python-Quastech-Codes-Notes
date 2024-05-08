from django.urls import path,include
from . import views as v
urlpatterns=[
    path("donorhome",v.donorhome),
    path("add-food",v.addFood),
    path("delete-food/<int:pk>",v.deleteFood),
    path("edit-food/<int:pk>",v.editFood),
    path("requests",v.requests)

]

