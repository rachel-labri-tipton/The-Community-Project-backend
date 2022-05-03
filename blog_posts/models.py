from django.db import models
from django.utils import timezone
from authors.models import Author
from blog_categories.models import Category
from users.models import User

# Create your models here.

class BlogPost(models.Model):

    class BlogPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset.filter(status='published')

    OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ManyToManyField(
        Category, blank=True)
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_name', null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=True)
    status = models.CharField(
        max_length=10, choices=OPTIONS, default='published')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    postobjects = BlogPostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
