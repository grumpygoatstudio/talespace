from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Tale(models.Model):
    title = models.CharField(max_length=40)
    userId = models.ForeignKey(User)
    content = models.TextField()

    def __str__(self):
        return self.title