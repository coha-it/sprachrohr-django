from django.shortcuts import render

# Create your views here.
from .models import Post, Author, Source
from django.http import JsonResponse
from django.core import serializers


class PostView():
    def list(self):

        print(
            Post.objects.first()
        )

        posts = list(Post.objects.all().filter().values())
        for post in posts:
            sources = list(Source.objects.filter(post=post['id']).values())
            if sources:
                post['sources'] = sources

            authors = list(Author.objects.filter(post=post['id']).values())
            if authors:
                post['authors'] = authors
        return JsonResponse(posts, safe=False)
