from django.urls import path
from .views import PostView

urlpatterns = [
    path('podcasts', PostView.list, name='post-list'),
]
