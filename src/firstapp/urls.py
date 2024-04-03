from django.urls import path
from . import views as v
urlpatterns = [
    path("fourth",v.fourth),
    path("fifth",v.fifth)
]