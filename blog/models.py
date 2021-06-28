from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import SlugField
from django.utils.text import slugify
from django.db.models.fields.files import ImageField
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.date}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)