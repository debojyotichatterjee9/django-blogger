from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

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
class DetailPostView(View):

    def is_stored_post(self, request, post_id):
        is_saved_for_later = False
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None or len(stored_posts) > 0:
            is_saved_for_later = post_id in stored_posts
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        is_saved_for_later = self.is_stored_post(request, post.id)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-date"),
            "is_saved_for_later": is_saved_for_later
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        is_saved_for_later = self.is_stored_post(request, post.id)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # does not hit the db but creates an instance
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog-detail", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date"),
            "is_saved_for_later": is_saved_for_later
        }
        return render(request, "blog/post-detail.html", context)



class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["posts_saved"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["posts_saved"] = True
        print(context)
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])
        post_slug = request.POST["post_slug"]
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
        
        return redirect("blog-detail", post_slug)