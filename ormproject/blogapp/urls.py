from django.urls import path
from . import views as v
urlpatterns = [
    path("blogs/add",v.addBlog),
    path("blogs/view",v.viewBlog)
]