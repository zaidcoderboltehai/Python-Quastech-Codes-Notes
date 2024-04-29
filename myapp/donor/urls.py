from django.urls import path,include
from . import views as v
urlpatterns=[
    path("donorhome",v.donorhome),
    path("add-food",v.addFood)

]