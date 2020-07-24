from django.urls import path
from .views import PostView

urlpatterns = [
    path('posts/list', PostView.list, name='post-list'),
]
