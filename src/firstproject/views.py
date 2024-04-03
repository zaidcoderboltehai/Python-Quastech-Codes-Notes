from django.shortcuts import HttpResponse

def home(request):
    data="""
<h1>welcome to home page</h1>
<a href="firsturl">first page</a>
<a href="secondurl">second page</a>
<a href="thirdurl">third page</a>
"""
    return HttpResponse(data)

def firstView(request):
    data="""
<h1>welcome to first page</h1>
<a href="secondurl">second page</a>
<a href="thirdurl">third page</a>
<a href="/">home page</a>
"""
    return HttpResponse(data)

def secondView(request):
    data="""
<h1>welcome to second page</h1>
<a href="firsturl">first page</a>
<a href="thirdurl">third page</a>
<a href="/">home page</a>
"""
    return HttpResponse(data)

def thirdView(request):
    data="""
<h1>welcome to third page</h1>
<a href="firsturl">first page</a>
<a href="secondurl">second page</a>
<a href="/">home page</a>
"""
    return HttpResponse(data)

