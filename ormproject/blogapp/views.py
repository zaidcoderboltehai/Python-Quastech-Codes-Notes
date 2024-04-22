from django.shortcuts import render,redirect
from firstapp.models import User
from .models import Blog

def addBlog(request,pk):
    if(request.method == "POST"):
        title = request.POST.get("title")
        description = request.POST.get("description")
        img=request.FILES.get("img")
        blog=Blog()
        blog.title=title
        blog.description=description
        blog.blog_image=img
        blog.user= User.objects.get(id=pk)
        blog.save()
        return redirect("/list")
    else:
        return render(request,"addblog.html")