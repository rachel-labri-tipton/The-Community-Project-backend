

from rest_framework import serializers
from blog_posts.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'author', 'excerpt',
                  'content', 'status', 'image')
