from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    display_name = models.CharField(max_length=50)
    bio          = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.display_name)


class Post(models.Model):
    active      = models.BooleanField(default=False)
    url         = models.CharField(max_length=255, unique=True)
    title       = models.CharField(max_length=255, null=True, blank=True)
    date        = models.DateField(null=True, blank=True)
    desc_short  = models.TextField(null=True, blank=True)
    desc_long   = models.TextField(null=True, blank=True)
    img_url     = models.CharField(max_length=255, null=True, blank=True)
    type        = models.CharField(max_length=1, choices=(
        ('A', 'Audio-Blogpost'),
        ('S', 'Text-Blogpost'),
    ))

    author      = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Source(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    prio    = models.IntegerField(null=True, blank=True)
    src     = models.TextField(null=True, blank=True)
    type    = models.TextField(null=True, blank=True)

    def __str__(self):
        return "(On %s): %s" % (self.post.title, self.src)
