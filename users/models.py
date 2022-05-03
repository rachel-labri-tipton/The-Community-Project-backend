from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CommunityUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(null=True)
