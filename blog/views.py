from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.response import Http404
from datetime import date
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm

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
    context_object_name = "all_posts"

    def get_queryset(self):
        return super().get_queryset()


# post detail
class DetailPostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context