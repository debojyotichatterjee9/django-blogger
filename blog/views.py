from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import Http404


# Create your views here.

all_posts = {
    
}
# landing page
def home(request):
    try:
        # this is a shortcut method
        return render(request, "blog/index.html")
    except:
        raise Http404()

# post list


def posts(request):
    try:
        # this is a shortcut method
        return render(request, "blog/all-posts.html", {
            "all_posts": all_posts
        })
    except:
        raise Http404()

# post detail


def post_detail(request, slug):
    try:
        # this is a shortcut method
        return render(request, "blog/post-detail.html")
    except:
        raise Http404()
