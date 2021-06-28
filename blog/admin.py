from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date"]
    list_filter = ["author", "date", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("slug",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["caption"]


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)