from django.contrib import admin
from django.urls import path
from .views import firstView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("firsturl",firstView)
]




