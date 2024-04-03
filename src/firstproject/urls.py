from django.contrib import admin
from django.urls import path,include
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",v.home),
    path("firsturl",v.firstView),
    path("secondurl",v.secondView),
    path("thirdurl",v.thirdView),
    path("",include("firstapp.urls")),
    path("",include("secondapp.urls"))
]
