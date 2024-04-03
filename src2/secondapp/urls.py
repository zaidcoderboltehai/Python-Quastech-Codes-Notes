from django.urls import path
from . import views

urlpatterns = [
    path('', views.third_view, name='third_view'),
    path('fourth', views.fourth_view, name='fourth_view'),
]
