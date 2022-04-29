from django.urls import path
from .views import BlogPostsView


urlpatterns = [
    path("", BlogPostsView.as_view()),
]
