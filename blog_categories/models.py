
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
