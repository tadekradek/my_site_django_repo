from datetime import date

from django.shortcuts import render

all_posts = [
    {"slug":"ligunia",
     "img":"liga.png",
     "author":"radek",
     "date": date(2022,11,5),
     "title":"Liga Legend",
     "excert":"Welcome to the league of Draven",
     "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit"},
    {"slug":"spotify",
     "img":"spotify.png",
     "author":"radek",
     "date": date(2022,11,6),
     "title":"Spotify",
     "excert":"Spotify Logo",
     "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit"},
    {"slug":"github",
     "img":"github.png",
     "author":"radek",
     "date": date(2022,11,7),
     "title":"Github Desktop",
     "excert":"Github Desktop Icon",
     "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit."}
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/all-posts.html",{"posts": latest_posts})

def post_detail(request, slug):  #if you have dynamic url in urlpatters with slug, this function needs to receive another argument
    return render(request, "blog/post-detail.html")
