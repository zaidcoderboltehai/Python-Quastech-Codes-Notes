from django.urls import path
from . import views as v
urlpatterns = [
    path("blog/add/<int:pk>",v.addBlog),
]