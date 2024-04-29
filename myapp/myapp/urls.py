from django.contrib import admin
from django.urls import path,include
from user.views import loginpage,signup,logoutuser

urlpatterns = [
    path("",loginpage),
    path("signup",signup),
    path('admin/', admin.site.urls),
    path("logout",logoutuser),
    path("",include('user.urls')),
    path("",include('donor.urls'))
]

