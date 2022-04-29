from django.shortcuts import render
from rest_framework import generics

from blog_posts.models import BlogPosts
from blog_posts.serializers import BlogPostsSerializer
# Create your views here.


class BlogPostsView(generics.ListCreateAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer
