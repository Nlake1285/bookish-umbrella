# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home_page_view(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})
    # return HttpResponse("Hello, World!")