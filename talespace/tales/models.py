from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

class Tale(models.Model):
    title = models.CharField(max_length=40)
    author_id = models.ForeignKey(User)
    content = models.TextField()
    header_img = models.URLField(default="#")

    def __str__(self):
        return self.title