from django.urls import path
from . import views as v
urlpatterns = [
    path("blog/add/<int:pk>",v.addBlog),
    path("blog/view/<int:pk>",v.viewBlog)
]