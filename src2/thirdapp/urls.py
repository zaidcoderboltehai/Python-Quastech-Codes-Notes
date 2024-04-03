# thirdapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='thirdapp_contact'),
    path('faq/', views.faq, name='thirdapp_faq'),
]
