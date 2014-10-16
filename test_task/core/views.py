from django.shortcuts import render
from models import CustomUser, Post

def home_view(request):
    posts = Post.objects.order_by("-id")
    return render(request, "home.html", {"posts":posts})
