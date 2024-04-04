from django.urls import path
from . import views as v
urlpatterns = [
    path("",v.home),
    path("first",v.first),
    path("second",v.second)
]