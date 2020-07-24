from django.contrib import admin

# Register your models here.
from .models import Author, Post, Source, Tag

admin.site.register([Author, Post, Source, Tag])
