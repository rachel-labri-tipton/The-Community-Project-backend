from django.db import models
from djrichtextfield.models import RichTextField
# Create your models here.

from djrichtextfield.models import RichTextField


class BlogPosts(models.Model):
    content = RichTextField()
