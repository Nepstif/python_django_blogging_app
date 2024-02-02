from django.http import Http404
from django.shortcuts import render, get_object_or_404 as get_object

from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  "blog/post/list.html",
                  {"posts": posts})


def post_detail(request, id):
    post = get_object(Post, id=id, status=Post.Status.PUBLISHED)

    return render(request, "blog/post/detail.html",
                  {"post": post})
