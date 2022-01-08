from django.db import models


class Tutorial(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
