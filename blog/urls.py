from django.urls import path

from . import views

urlpatterns = [  #for every url pattern that you are adding here, you need to have respective view logic
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page") #/posts/my-first-post - this is a concept called slug
]