from rest_framework import serializers
from blog_posts.models import BlogPosts


class BlogPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPosts
        fields = '__all__'

    def __str__(self):
        return f'{self.content}'
