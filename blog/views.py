from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

# landing page
def home(request):
    return HttpResponse("Home Page!!!")

# post list
def posts(request):
    return HttpResponse("Post List!!!")

# post detail
def post_detail(request):
    return HttpResponse("Post Detail!!!")
