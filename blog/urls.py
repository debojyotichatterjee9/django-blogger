from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="blog-home"),
    path("posts", views.AllPostsView.as_view(), name="blog-list"),
    path("post/<slug:slug>", views.DetailPostView.as_view(), name="blog-detail")
]
