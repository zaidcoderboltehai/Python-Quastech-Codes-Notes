from django.shortcuts import render,redirect
from firstapp.models import User
from .models import Blog


def addBlog(request):
    if(request.method == "POST"):
        title = request.POST.get("title")
        description = request.POST.get("description")
        img=request.FILES.get("img")
        blog=Blog()
        blog.title=title
        blog.description=description
        blog.blog_image=img
        blog.user=request.user
        blog.save()
        return redirect("/blogs/view")
    else:
        return render(request,"addblog.html")
    
def viewBlog(request):
    blogs=Blog.objects.filter(user=request.user)
    return render(request,"bloglist.html",{"blogs":blogs})