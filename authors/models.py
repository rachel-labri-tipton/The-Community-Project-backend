
from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50, default="Harriet")
    last_name = models.CharField(max_length=50, default="Smith")
    bio = models.TextField(max_length=250, default='artist bio')
    # blogposts=models.ManyToOneRel(BlogPost, related_name='author_posts', on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
