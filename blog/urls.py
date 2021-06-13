from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("posts", views.posts, name="blog-list"),
    path("posts/<slug:slug>", views.post_detail, name="blog-detail"),
]
