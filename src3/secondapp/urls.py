from django.urls import path
from . import views as v
urlpatterns = [
    path("third",v.third),
    path("fourth",v.fourth)
]