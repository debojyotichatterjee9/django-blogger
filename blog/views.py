from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.response import Http404
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "hike-mountains",
        "image": "mountains.jpg",
        "author": "Fred Barner",
        "date": date(2021, 7, 20),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex labore voluptate...",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minus reiciendis veniam inventore eligendi ad corporis unde a 
        recusandae nostrum quos aliquam ullam, cum repellendus doloremque 
        fuga voluptas suscipit velit iste.
        """

    },
    {
        "slug": "new-laptop",
        "image": "laptop.jpg",
        "author": "Fred Barner",
        "date": date(2021, 7, 5),
        "title": "New laptop",
        "excerpt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex labore voluptate...",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minus reiciendis veniam inventore eligendi ad corporis unde a 
        recusandae nostrum quos aliquam ullam, cum repellendus doloremque 
        fuga voluptas suscipit velit iste.
        """

    },
    {
        "slug": "forest-tour",
        "image": "forest.jpg",
        "author": "Fred Barner",
        "date": date(2021, 12, 20),
        "title": "Forest Tour",
        "excerpt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex labore voluptate...",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minus reiciendis veniam inventore eligendi ad corporis unde a 
        recusandae nostrum quos aliquam ullam, cum repellendus doloremque 
        fuga voluptas suscipit velit iste.
        """

    },
    {
        "slug": "tech-stuff",
        "image": "laptop.jpg",
        "author": "Fred Barner",
        "date": date(2021, 3, 15),
        "title": "Tech Stuff",
        "excerpt": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex labore voluptate...",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Minus reiciendis veniam inventore eligendi ad corporis unde a 
        recusandae nostrum quos aliquam ullam, cum repellendus doloremque 
        fuga voluptas suscipit velit iste.
        """

    }
]
def get_date(post):
    return post['date']
# landing page
def home(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-2:]
    try:
        # this is a shortcut method
        return render(request, "blog/index.html", {
            "posts": latest_posts
        })
    except Exception as e:
        return HttpResponseNotFound(e)

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
