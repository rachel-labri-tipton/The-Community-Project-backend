from django.db import models
from users.models import User

# Create your models here.


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    bio = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
