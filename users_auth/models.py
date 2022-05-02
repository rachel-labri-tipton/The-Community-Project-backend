from django.db import models
from django.contrib.auth.models import (AbstractUser)
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(null=True)
    # conversations = models.ManyToManyField(Chatroom, on_delete=models.SET_NULL,)
    is_author = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
