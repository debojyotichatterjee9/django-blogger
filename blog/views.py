from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import Http404


# Create your views here.

# landing page
def home(request):
    try:
        # this is a shortcut method
        return render(request, "blog/index.html")
    except:
        raise Http404()

# post list


def posts(request):
    return HttpResponse("Post List!!!")

# post detail


def post_detail(request):
    return HttpResponse("Post Detail!!!")
