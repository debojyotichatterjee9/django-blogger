from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.response import Http404
from datetime import date
from django.views.generic import ListView
from .models import Post

# custom function
def get_date(post):
    return post['date']

# landing page
class HomePageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:2]
        return data


# post list
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        return super().get_queryset()

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
