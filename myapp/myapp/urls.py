from django.contrib import admin
from django.urls import path,include
from user.views import loginpage,signup

urlpatterns = [
    path("",loginpage),
    path("signup",signup),
    path('admin/', admin.site.urls),
    path('user',include('user.urls')),
    path('donor',include('donor.urls'))
]
