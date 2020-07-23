from django.shortcuts import render

# Create your views here.
from .models import Post
from django.http import JsonResponse
from django.core import serializers


class PostView():
    def list(self):
        posts = list(Post.objects.all().filter().values())
        data = serializers.serialize("json", Post.objects.all())

        return JsonResponse(posts, safe=False)
