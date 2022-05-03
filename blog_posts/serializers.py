

from authors.models import Author
from blog_categories.models import Category
from rest_framework import serializers
from blog_posts.models import BlogPost
from users.models import CommunityUser

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'bio')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer
    class Meta:
        model = BlogPost
        fields = '__all__'
    
    def validate(self, attrs):
        #adds custom validation
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            if request.user.is_writer==False:
                raise serializers.ValidationError({
                    "is_writer": "Only writers are allowed to create and update blog posts."
                })
        return attrs
    
    def create(self, data):
        author_data = data.pop("author")
        category_data = data.pop("category")

        blogpost = BlogPost( 
            title=data[]


        )

