from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.response import Http404
from datetime import date
from .models import Post


def get_date(post):
    return post['date']
# landing page
def home(request):
    all_posts = Post.objects.all().order_by("-date")[:3]
    try:
        # this is a shortcut method
        return render(request, "blog/index.html", {
            "posts": all_posts
        })
    except Exception as e:
        return HttpResponseNotFound(e)

# post list


def posts(request):
    try:
        all_posts = Post.objects.all().order_by("-date")
        return render(request, "blog/all-posts.html", {
            "all_posts": all_posts
        })
    except:
        raise Http404()

# post detail


def post_detail(request, slug):
    identified_post =  Post.objects.get(slug=slug)
    print(identified_post)
    # try:
        # this is a shortcut method
    return render(request, "blog/post-detail.html", {
            "post": identified_post,
            "post_tags": identified_post.tags.all()
        })
    # except:
        # raise Http404()
