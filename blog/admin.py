from django.contrib import admin
from .models import Post, Author, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date"]
    list_filter = ["author", "date", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("slug",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["caption"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["guest_name", "guest_email", "date"]
    list_filter = ["date"]

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)